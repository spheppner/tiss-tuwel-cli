# Examples

## ToDo-List-Integration

This example is assuming a db containing the following table: `activity (id INT PRIMARY KEY, name VARCHAR(255), duedate INT)`

Also the config file is expected to have the following structure:

```js
module.exports = {
    ws_token: 'YOUR_API_TOKEN',
    todoist_token: 'YOUR_TODOIST_TOKEN',
    project_parent: 'PROJECT_NAME_FOR_TASKS', //e.g. 'TUWEL', 'UNI' needs to exist in todoist
    clientUrl: 'tuwel.tuwien.ac.at',
    clientConfig: {
        protocol: 'https',
        port: '443',
        subdirectory: ''
    }
}
```

We want to add assignments, checkmarks and quizzes to todoist. But as we do not want to recreate tasks, we handle existence-checking
with a sqlite db.

```js

const sqlite3 = require('sqlite3').verbose()
const todoist = require('todoist-nodejs');

const config = require('./config')
const {
    MoodleRestClient
} = require('./moodle-rest-client')

let db = new sqlite3.Database('./db/tuwel_tudo.db');


sql_query_activity = "SELECT id FROM activity;"
sql_insert_activity_template = "INSERT INTO activity VALUES "

activities = []

const api = new todoist(config.todoist_token);
// id calculation beacuse each module has its own auto increment id, this is an easy way to ensure uniqueness for the db.
async function assign_callback(course_data) {
    course_data.assignments.forEach(ass => activities.push({
        id: ass.id*10+1,
        name: ass.name,
        duedate: ass.duedate
    }))
}
async function checkmark_callback(data) {
    data.checkmarks.forEach(ch => activities.push({
        id: ch.id*10+2,
        name: ch.name,
        duedate: ch.timedue
    }))
}
async function quiz_callback(data) {
    console.log(data)
    data.quizzes.forEach(quiz => activities.push({
        id: quiz.id*10+3,
        name: quiz.name,
        duedate: quiz.timeopen  
    }))
}
async function get_tuwel_data() {
    client = new MoodleRestClient(config.clientUrl, config.ws_token, config.clientConfig)

    await client.send('mod_assign_get_assignments', {}).then(res => res.courses.forEach(assign_callback), console.log)
    await client.send('mod_checkmark_get_checkmarks_by_courses', {}).then(checkmark_callback, console.log)
    await client.send('mod_quiz_get_quizzes_by_courses', {}).then(quiz_callback, console.log)
}

function select(sql) {
    return new Promise((resolve, reject) => {
        const res = [];
        db.each(sql, (err, row) => {
            if (err) {
                reject(err); // optional: you might choose to swallow errors.
            } else {
                res.push(row); // accumulate the data
            }
        }, (err, n) => {
            if (err) {
                reject(err); // optional: again, you might choose to swallow this error.
            } else {
                resolve(res); // resolve the promise
            }
        });
    });
}

async function filter_out_old() {
    let old_activity_ids;
    await select(sql_query_activity).then(res => old_activity_ids = res.map(act => act.id), console.log)
    console.log(old_activity_ids)
    activities = activities.filter(act => old_activity_ids.indexOf(act.id) == -1)
}

async function add_todo_tasks() {
    console.log(activities)
    let parent_id;
    await api.sync().then(res => parent_id = res.data.projects.find(project => project.name == config.project_parent).id);


    activity_add_promises = activities.map(activity => api.items.add(activity.name, {
        project_id: parent_id
    }))
    try { //there is some issue in the todoist module throwing an error, while still performing the commit.
        await Promise.all(activity_add_promises)
        await api.commit()
    } catch {}
}

function store_new_tasks() {
    if (activities.length > 0) {
        const placeholders = activities.map(act => `(${act.id},'${act.name}',${act.duedate})`).join(', ')
        console.log(sql_insert_activity_template + placeholders)
        db.run(sql_insert_activity_template + placeholders)
    }
}


get_tuwel_data().then(filter_out_old).then(add_todo_tasks).then(store_new_tasks).then(() => db.close())
```

## Reading Grades

For each course in progress, we create a pandas-dataframe representing the course-grades.

```python
import pandas as pd
from moodle_client import MoodleClient

token = 'YOUR_API_TOKEN'
client = MoodleClient(token, 'https://tuwel.tuwien.ac.at')

courses = client.send('core_course_get_enrolled_courses_by_timeline_classification', {'classification': 'inprogress'}).courses
course_ids = [c.id for c in courses]

course_grade_dfs = {}
for course_id in course_ids:
    gradeitems = client.send('gradereport_user_get_grade_items', {'courseid': course_id, 'userid': 4}).usergrades[0].gradeitems[:-1]
    name = [i.itemname for i in gradeitems]
    grade = [i.graderaw for i in gradeitems]
    grademin = [i.grademin for i in gradeitems]
    grademax = [i.grademax for i in gradeitems]
    course_grade_df = pd.DataFrame({'name': name, 'grade': grade, 'grademin': grademin, 'grademax': grademax})
    course_grade_dfs[course_id] = course_grade_df
    print(course_grade_df)
```