<?php

/**
 * Prints the external functions in markdown format for the documentation in mkdocs
 */

require_once('../../config.php');
require_once($CFG->libdir . '/adminlib.php');
require($CFG->dirroot . '/webservice/lib.php');

admin_externalpage_setup('webservicedocumentation');

$curated_functions = ['ModCheckmark' => [
    'mod_checkmark_get_checkmarks_by_courses',
    'mod_checkmark_get_checkmark',
    'mod_checkmark_submit',
],
    'ModGrouptool' => [
        'mod_grouptool_get_grouptools_by_courses',
        'mod_grouptool_get_grouptool',
        'mod_grouptool_register',
        'mod_grouptool_deregister',
        'mod_grouptool_change_group',
        'mod_grouptool_get_registration_status',
    ],
    'ModOfflinequiz' => [
        'mod_offlinequiz_get_offlinequizzes_by_courses',
        'mod_offlinequiz_get_offlinequiz',
        'mod_offlienquiz_get_attempt_review',
    ],
    'ModOrganizer' => [
        'mod_organizer_get_organizers_by_courses',
        'mod_organizer_get_organizer',
        'mod_organizer_get_slots',
        'mod_organizer_register_appointment',
        'mod_organizer_unregister_appointment',
        'mod_organizer_reregister_appointment',
        'mod_organizer_get_appointment_status',
    ],
    'ModPublication' => [
        'mod_publication_get_publications_by_courses',
        'mod_publication_get_publication',
    ],
    'CoreCalendar' => [
        'core_calendar_create_calendar_events',
        'core_calendar_delete_calendar_events',
        'core_calendar_get_action_events_by_course',
        'core_calendar_get_action_events_by_courses',
        'core_calendar_get_action_events_by_timesort',
        'core_calendar_get_calendar_day_view',
        'core_calendar_get_calendar_events',
        'core_calendar_get_calendar_event_by_id',
        'core_calendar_get_calendar_upcoming_view',
        'core_calendar_get_timestamps',
        'core_calendar_update_event_start_day',
    ],
    'CoreCourse' => [
        'core_course_get_contents',
        'core_course_get_courses_by_field',
        'core_course_get_course_module',
        'core_course_get_enrolled_courses_by_timeline_classification',
        'core_course_search_courses',
        'core_course_set_favourite_courses',
    ],
    'Gradereport' => [
        'gradereport_overview_get_course_grades',
        'gradereport_user_get_grades_table',
        'gradereport_user_get_grade_items',
    ],
    'ModAssign' => [
        'mod_assign_get_assignments',
        'mod_assign_get_submission_status',
        'mod_assign_save_submission',
        'mod_assign_submit_for_grading',
    ],
    'ModBook' => [
        'mod_book_get_books_by_courses',
    ],
    'ModChoice' => [
        'mod_choice_delete_choice_responses',
        'mod_choice_get_choices_by_courses',
        'mod_choice_get_choice_options',
        'mod_choice_submit_choice_response',
    ],
    'ModData' => [
        'mod_data_get_databases_by_courses',
        'mod_data_get_data_access_information',
        'mod_data_get_entries',
        'mod_data_get_entry',
        'mod_data_get_fields',
        'mod_data_search_entries',
    ],
    'ModFeedback' => [
        'mod_feedback_get_feedbacks_by_courses',
        'mod_feedback_get_feedback_access_information',
        'mod_feedback_get_finished_responses',
        'mod_feedback_get_items',
        'mod_feedback_get_last_completed',
        'mod_feedback_get_page_items',
    ],
    'ModFolder' => [
        'mod_folder_get_folders_by_courses',
    ],
    'ModForum' => [
        'mod_forum_add_discussion',
        'mod_forum_add_discussion_post',
        'mod_forum_can_add_discussion',
        'mod_forum_delete_post',
        'mod_forum_get_discussion_post',
        'mod_forum_get_discussion_posts',
        'mod_forum_get_discussion_posts_by_userid',
        'mod_forum_get_forums_by_courses',
        'mod_forum_get_forum_access_information',
        'mod_forum_get_forum_discussions',
        'mod_forum_get_forum_discussions_paginated',
        'mod_forum_get_forum_discussion_posts',
        'mod_forum_set_subscription_state',
        'mod_forum_toggle_favourite_state',
    ],
    'ModGlossary' => [
        'mod_glossary_get_authors',
        'mod_glossary_get_categories',
        'mod_glossary_get_entries_by_author',
        'mod_glossary_get_entries_by_author_id',
        'mod_glossary_get_entries_by_category',
        'mod_glossary_get_entries_by_date',
        'mod_glossary_get_entries_by_letter',
        'mod_glossary_get_entries_by_search',
        'mod_glossary_get_entries_by_term',
        'mod_glossary_get_entry_by_id',
        'mod_glossary_get_glossaries_by_courses',
    ],
    'ModLesson' => [
        'mod_lesson_get_lesson',
        'mod_lesson_get_lessons_by_courses',
        'mod_lesson_get_lesson_access_information',
        'mod_lesson_get_pages',
        'mod_lesson_get_page_data',
        'mod_lesson_get_questions_attempts',
        'mod_lesson_get_user_attempt',
        'mod_lesson_get_user_attempt_grade',
        'mod_lesson_get_user_grade',
    ],
    'ModPage' => [
        'mod_page_get_pages_by_courses',
    ],
    'ModQuiz' => [
        'mod_quiz_get_attempt_access_information',
        'mod_quiz_get_attempt_review',
        'mod_quiz_get_combined_review_options',
        'mod_quiz_get_quizzes_by_courses',
        'mod_quiz_get_quiz_access_information',
        'mod_quiz_get_quiz_required_qtypes',
        'mod_quiz_get_user_attempts',
        'mod_quiz_get_user_best_grade',
    ],
    'ModResource' => [
        'mod_resource_get_resources_by_courses',
    ],
    'ModSurvey' => [
        'mod_survey_get_questions',
        'mod_survey_get_surveys_by_courses',
    ],
    'ModUrl' => [
        'mod_url_get_urls_by_courses',
    ],
    'ModWiki' => [
        'mod_wiki_get_page_contents',
        'mod_wiki_get_subwikis',
        'mod_wiki_get_subwiki_files',
        'mod_wiki_get_subwiki_pages',
        'mod_wiki_get_wikis_by_courses',
    ],
    'ModWorkshop' => [
        'mod_workshop_get_assessment',
        'mod_workshop_get_grades',
        'mod_workshop_get_reviewer_assessments',
        'mod_workshop_get_submission',
        'mod_workshop_get_submissions',
        'mod_workshop_get_submission_assessments',
        'mod_workshop_get_user_plan',
        'mod_workshop_get_workshops_by_courses',
        'mod_workshop_get_workshop_access_information',
    ],
    'block' => [
        'block_recentlyaccesseditems_get_recent_items',
        'block_starredcourses_get_starred_courses',
    ],
];

// get all the function descriptions
$functions = $DB->get_records('external_functions', array('services' => 'moodle_mobile_app'), 'name');
$functiondescs = array();
foreach ($functions as $function) {
    $functiondescs[$function->name] = external_api::external_function_info($function);
}

$documentationhtml = "";
$br = html_writer::empty_tag('br', array());

function printParams($params, $indent = "") {
    foreach ($params as $key => $value) {
        echo $indent . $key . " ";


        if (!empty($value->content)) {
            if ($value->required == 2) {
                echo "**Optional** ";
            }
            echo "// $value->desc" . "\n";

            echo $indent . "[" . "\n";
            echo $indent . "\t{" . "\n";
            if (!empty($value->content->keys)) {
                printParams($value->content->keys, $indent . "\t\t");
            }else {
                echo "\t\t";
                printParam($value->content);
            }

            echo $indent . "\t}" . "\n";
            echo $indent . "]" . "\n";

        } else if (!empty($value->keys)) {
            if ($value->required == 2) {
                echo "**Optional** ";
            }
            echo "// $value->desc" . "\n";

            echo $indent . "{" . "\n";
            printParams($value->keys, $indent . "\t");
            echo $indent . "}" . "\n";

        } else {
            printParam($value);
        }

    }
}


function printParam($value) {
    switch ($value->type) {
        case PARAM_BOOL: // 0 or 1 only for now
        case PARAM_INT:
            $type = 'int';
            break;
        case PARAM_FLOAT;
            $type = 'double';
            break;
        default:
            $type = 'string';
    }
    echo "$type ";
    if ($value->required == 2) {
        echo "**Optional** ";
    }
    echo "// $value->desc" . "\n";
}

echo '<table class="wrapped relative-table confluenceTable docutils">
<colgroup><col style="width: 10.6716%;"><col style="width: 33.209%;"></colgroup>
<tbody>';
foreach($curated_functions as $title => $fs) {
    echo '<tr>';
    echo '<td>';
    echo "<strong>$title</strong>";
    echo '</td>';
    echo '<td>';
    foreach($fs as $f) {

        foreach ($functions as $id => $function) {
            if (strcmp($function->name, $f) == 0) {
                $description = $function;
                break;
            }
        }

        echo "<details>";
        echo "\n";

        echo "<summary>$description->name</summary>";
        echo "\n";
        echo "<br/>";
        echo "\n";

        echo "<p>$description->description</p>";
        echo "\n";

        echo "<h3>Parameters</h3>";
        echo "\n";

        if (!empty($description->parameters_desc->keys)) {
            echo "```" . "\n";
            printParams($description->parameters_desc->keys);
            echo "```" . "\n";
        }else {
            echo "<strong>No Parameters.</strong><br/>";
            echo "\n";
        }

        echo "\n";
        echo "<h3>Returns</h3>";
        echo "\n";

        if (!empty($description->returns_desc->keys)) {
            echo "```" . "\n";
            printParams($description->returns_desc->keys);
            echo "```" . "\n";
        }else {
            echo "<strong>No Return.</strong><br/>";
            echo "\n";
        }

        echo "\n";

        echo "<hr/>";
        echo "\n";

        echo "</details>";
        echo "\n";
    }
    echo '</td>';
    echo '</tr>';

}

echo '</tbody></table>';

