# Curated Functions

There are many functions that are either inaccessible, or irrelevant to students. 
Find the following list of features and their functions. It contains those we tried, and found to be potentially useful to students.

See [Function Documentation](all_functions.md) for information on all functions.


** TODO: at the time of writing the functions of the first 5 features (the AMC plugins) are not implemented. At time of publishing update this accordingly. ** 

<table class="wrapped relative-table confluenceTable docutils">
<colgroup><col style="width: 10.6716%;"><col style="width: 33.209%;"></colgroup>
<tbody><tr><td><strong>ModCheckmark</strong></td><td><details>
<summary>mod_checkmark_get_checkmarks_by_courses</summary>
<br/>
<p>Get all checkmarks in the given courses</p>
<h3>Parameters</h3>
```
courseids // Array of course ids (all enrolled courses if empty array)
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
checkmarks // All checkmarks for the given courses
[
	{
		id int // checkmark id
		instance int // checkmark instance id
		course int // course id the checkmark belongs to
		name string // checkmark name
		intro string // intro/description of the checkmark
		introformat int // intro format
		timedue int // time due of the checkmark
		cutoffdate int // cutoff date of the checkmark
		submission_timecreated int **Optional** // submission created
		submission_timemodified int **Optional** // submission changed
		examples // Examples
		[
			{
				id int // example id
				name string // example name
				checked int **Optional** // example checked state
			}
		]
		feedback **Optional** // submission information
		{
			grade string // Grade
			feedback string // Feedback comment
			feedbackformat int // Feedback comment format
			timecreated int // Time the feedback was given
			timemodified int // Time the feedback was modified
		}
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_checkmark_get_checkmark</summary>
<br/>
<p>Get the checkmark with the given id</p>
<h3>Parameters</h3>
```
checkmarkid int // The id of the checkmark
```

<h3>Returns</h3>
```
checkmark // example information
{
	id int // checkmark id
	instance int // checkmark instance id
	course int // course id the checkmark belongs to
	name string // checkmark name
	intro string // intro/description of the checkmark
	introformat int // intro format
	timedue int // time due of the checkmark
	cutoffdate int // cutoff date of the checkmark
	submission_timecreated int **Optional** // submission created
	submission_timemodified int **Optional** // submission changed
	examples // Examples
	[
		{
			id int // example id
			name string // example name
			checked int **Optional** // example checked state
		}
	]
	feedback **Optional** // submission information
	{
		grade string // Grade
		feedback string // Feedback comment
		feedbackformat int // Feedback comment format
		timecreated int // Time the feedback was given
		timemodified int // Time the feedback was modified
	}
}
```

<hr/>
</details>
<details>
<summary>mod_checkmark_submit</summary>
<br/>
<p>Submit a submission for the checkmark with the given id</p>
<h3>Parameters</h3>
```
checkmarkid int // The id of the checkmark
submission_examples // The examples of the submission (must match the examples of the checkmark)
[
	{
		id int // example id
		name string **Optional** // example name
		checked int // example checked state
	}
]
```

<h3>Returns</h3>
```
checkmark // example information
{
	id int // checkmark id
	instance int // checkmark instance id
	course int // course id the checkmark belongs to
	name string // checkmark name
	intro string // intro/description of the checkmark
	introformat int // intro format
	timedue int // time due of the checkmark
	cutoffdate int // cutoff date of the checkmark
	submission_timecreated int **Optional** // submission created
	submission_timemodified int **Optional** // submission changed
	examples // Examples
	[
		{
			id int // example id
			name string // example name
			checked int **Optional** // example checked state
		}
	]
	feedback **Optional** // submission information
	{
		grade string // Grade
		feedback string // Feedback comment
		feedbackformat int // Feedback comment format
		timecreated int // Time the feedback was given
		timemodified int // Time the feedback was modified
	}
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModGrouptool</strong></td><td><details>
<summary>mod_grouptool_get_grouptools_by_courses</summary>
<br/>
<p>Get all grouptools for the given courses</p>
<h3>Parameters</h3>
```
courseids // Array of course ids (all enrolled courses if empty array)
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
grouptools // All grouptools for the given courses
[
	{
		id int // grouptool id
		instance int // grouptool instance id
		course int // course id the grouptool belongs to
		name string // grouptool name
		intro string // intro/description of the grouptool
		introformat int // intro format
		can_enter int // Is the user allowed to enter a group in this grouptool
		can_leave int // Is the user allowed to leave a group in this grouptool
		group_size int // Size of the groups
		groups // Groups of this grouptool
		[
			{
				id int // group id
				name string // group name
				group_size int // Size of this group
				rank string **Optional** // rank of registration or queue in this group
				registered int // number of users registered for this group
				queued int // number of users queued for this group
				registered_members **Optional** // registered members of the group if visible for current user
				[
					{
						user int // user id
					}
				]
				queued_members **Optional** // queued members of the group if visible for current user
				[
					{
						user int // user id
					}
				]
			}
		]
		user_registrations // Groups where the current user is registered or queued in
		{
			registered // Groups where the current user is registered
			[
				{
					id int // group id
					name string // group name
					rank string **Optional** // rank of registration or queue in this group
				}
			]
			queued // Groups where the current user is queued
			[
				{
					id int // group id
					name string // group name
					rank string **Optional** // rank of registration or queue in this group
				}
			]
		}
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_grouptool_get_grouptool</summary>
<br/>
<p>Get the grouptool with the given id</p>
<h3>Parameters</h3>
```
grouptoolid int // The id of the grouptool
```

<h3>Returns</h3>
```
grouptool // grouptool information
{
	id int // grouptool id
	instance int // grouptool instance id
	course int // course id the grouptool belongs to
	name string // grouptool name
	intro string // intro/description of the grouptool
	introformat int // intro format
	can_enter int // Is the user allowed to enter a group in this grouptool
	can_leave int // Is the user allowed to leave a group in this grouptool
	group_size int // Size of the groups
	groups // Groups of this grouptool
	[
		{
			id int // group id
			name string // group name
			group_size int // Size of this group
			rank string **Optional** // rank of registration or queue in this group
			registered int // number of users registered for this group
			queued int // number of users queued for this group
			registered_members **Optional** // registered members of the group if visible for current user
			[
				{
					user int // user id
				}
			]
			queued_members **Optional** // queued members of the group if visible for current user
			[
				{
					user int // user id
				}
			]
		}
	]
	user_registrations // Groups where the current user is registered or queued in
	{
		registered // Groups where the current user is registered
		[
			{
				id int // group id
				name string // group name
				rank string **Optional** // rank of registration or queue in this group
			}
		]
		queued // Groups where the current user is queued
		[
			{
				id int // group id
				name string // group name
				rank string **Optional** // rank of registration or queue in this group
			}
		]
	}
}
```

<hr/>
</details>
<details>
<summary>mod_grouptool_register</summary>
<br/>
<p>Register for group</p>
<h3>Parameters</h3>
```
grouptoolid int // grouptool id
id int // group id
```

<h3>Returns</h3>
```
message string // Message whether the registration was successful
```

<hr/>
</details>
<details>
<summary>mod_grouptool_deregister</summary>
<br/>
<p>deregister for group</p>
<h3>Parameters</h3>
```
grouptoolid int // grouptool id
id int // group id
```

<h3>Returns</h3>
```
message string // Message whether the un-registration was successful
```

<hr/>
</details>
<details>
<summary>mod_grouptool_change_group</summary>
<br/>
<p>Change from one group to another</p>
<h3>Parameters</h3>
```
grouptoolid int // grouptool id
id int // the id of the group where you want to be
```

<h3>Returns</h3>
```
message string // Message whether the change of group was successful
```

<hr/>
</details>
<details>
<summary>mod_grouptool_get_registration_status</summary>
<br/>
<p>Get the status of the current registration for this user in the given group tool</p>
<h3>Parameters</h3>
```
grouptoolid int // grouptool id
```

<h3>Returns</h3>
```
user_registrations // Groups where the current user is registered or queued in
{
	registered // Groups where the current user is registered
	[
		{
			id int // group id
			name string // group name
			rank string **Optional** // rank of registration or queue in this group
		}
	]
	queued // Groups where the current user is queued
	[
		{
			id int // group id
			name string // group name
			rank string **Optional** // rank of registration or queue in this group
		}
	]
}
```

<hr/>
</details>
</td></tr><tr><td><strong>ModOfflinequiz</strong></td><td><details>
<summary>mod_offlinequiz_get_offlinequizzes_by_courses</summary>
<br/>
<p>Get all offlinequizzes in the given courses</p>
<h3>Parameters</h3>
```
courseids // Array of course ids (all enrolled courses if empty array)
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
offlinequizzes // offlinequiz object
[
	{
		id int // offlinequiz id
		course int // course id the offlinequiz belongs to
		name string // offlinequiz name
		intro string **Optional** // Quiz introduction text.
		introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		time int **Optional** // Time of the quiz
		resultsavailable int **Optional** // whether allowed to view results and results exist
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // warnings
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_offlinequiz_get_offlinequiz</summary>
<br/>
<p>Get offlinequizze with the given id</p>
<h3>Parameters</h3>
```
offlinequizid int // offlinequiz id
```

<h3>Returns</h3>
```
offlinequiz // example information
{
	id int // offlinequiz id
	course int // course id the offlinequiz belongs to
	name string // offlinequiz name
	intro string **Optional** // Quiz introduction text.
	introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	introfiles **Optional** // Files in the introduction text
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for external files.
		}
	]
	time int **Optional** // Time of the quiz
	resultsavailable int **Optional** // whether allowed to view results and results exist
}
```

<hr/>
</details>
<details>
<summary>mod_offlinequiz_get_offlinequiz</summary>
<br/>
<p>Get offlinequizze with the given id</p>
<h3>Parameters</h3>
```
offlinequizid int // offlinequiz id
```

<h3>Returns</h3>
```
offlinequiz // example information
{
	id int // offlinequiz id
	course int // course id the offlinequiz belongs to
	name string // offlinequiz name
	intro string **Optional** // Quiz introduction text.
	introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	introfiles **Optional** // Files in the introduction text
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for external files.
		}
	]
	time int **Optional** // Time of the quiz
	resultsavailable int **Optional** // whether allowed to view results and results exist
}
```

<hr/>
</details>
</td></tr><tr><td><strong>ModOrganizer</strong></td><td><details>
<summary>mod_organizer_get_organizers_by_courses</summary>
<br/>
<p>Gets information on organizers in the provided courses (all courses if no ids are provided).</p>
<h3>Parameters</h3>
```
courseids // Array of course ids (all enrolled courses if empty array)
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
organizers // organizer info
[
	{
		id int // organizer id
		course int // course id the organizer belongs to
		name string // organizer name
		intro string **Optional** // organizer introduction text.
		introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		isgrouporganizer int **Optional** // Whether the organizer is a group organizer
		queue int **Optional** // organizer introduction text.
		allowregistrationsfromdate int **Optional** // start of registration period
		duedate int **Optional** // end of registration period
		relativedeadline int **Optional** // deadline for registering relative to a specific slot
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // warnings
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_organizer_get_organizer</summary>
<br/>
<p>Gets information of an organizer with the given id</p>
<h3>Parameters</h3>
```
organizerid int // The id of the organizer
```

<h3>Returns</h3>
```
organizer // organizer information
{
	id int // organizer id
	course int // course id the organizer belongs to
	name string // organizer name
	intro string **Optional** // organizer introduction text.
	introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	isgrouporganizer int **Optional** // Whether the organizer is a group organizer
	queue int **Optional** // organizer introduction text.
	allowregistrationsfromdate int **Optional** // start of registration period
	duedate int **Optional** // end of registration period
	relativedeadline int **Optional** // deadline for registering relative to a specific slot
}
```

<hr/>
</details>
<details>
<summary>mod_organizer_get_slots</summary>
<br/>
<p> Gets all appointment slots of the organizer with the provided id.</p>
<h3>Parameters</h3>
```
organizerid int // organizer id
```

<h3>Returns</h3>
```
organizer // organizer information
{
	id int // organizer id
	course int // course id the organizer belongs to
	name string // organizer name
	intro string **Optional** // organizer introduction text.
	introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	isgrouporganizer int **Optional** // Whether the organizer is a group organizer
	queue int **Optional** // organizer introduction text.
	allowregistrationsfromdate int **Optional** // start of registration period
	duedate int **Optional** // end of registration period
	relativedeadline int **Optional** // deadline for registering relative to a specific slot
}
slots // array of slots
[
	{
		id int // slot id
		organizerid int // organizer id
		starttime int // slot start time
		duration int // int format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string // slot location
		locationlink string // link to slot location
		maxparticipants int // maximum number of allowed participants (1 if groupmode)
		availablefrom int **Optional** // time relative to starttime when registration becomes possible
		teachervisible int // whether the teachers assigned to the slot are visible
		comments string **Optional** // slot comments
		isavailable int **Optional** // indicator whether the slot is available for registration
		isfull int **Optional** // indicator whether slot is full
		teachers // trainers (empty if not teachervisible)
		[
			{
				id int // user id
				firstname string // trainer firstname
				lastname string // trainer lastname
				email string // trainer email
			}
		]
	}
]
```

<hr/>
</details>
<details>
<summary>mod_organizer_register_appointment</summary>
<br/>
<p>Registers the current user for the slot with the provided id. If applicable, the user is added to the slot queue instead.</p>
<h3>Parameters</h3>
```
slotid int // slot id
```

<h3>Returns</h3>
```
appointmentid int // id of the new appointment (0 if not created)
queueid int // id of slot queue placement (0 if not created)
status int // indicator whether success (added to queue or appointment) or failure
```

<hr/>
</details>
<details>
<summary>mod_organizer_unregister_appointment</summary>
<br/>
<p>Unregisters the current user for the slot with the provided id. If applicable, the user is removed from the slot queue instead.</p>
<h3>Parameters</h3>
```
slotid int // Course id
```

<h3>Returns</h3>
```
status int // status indicator whether unregistering/dequeuing was successful
isunregister int // 1 if unregistering, 0 if dequeueing applies
```

<hr/>
</details>
<details>
<summary>mod_organizer_reregister_appointment</summary>
<br/>
<p>Reregisters the current user for the slot with the provided id. This is applicable, if the user is presently registered for another slot in the same organizer.</p>
<h3>Parameters</h3>
```
slotid int // slot id
```

<h3>Returns</h3>
```
status int // status indicator whether reregistering was successful
```

<hr/>
</details>
<details>
<summary>mod_organizer_get_appointment_status</summary>
<br/>
<p>Gets information on the current registered appointment for the given organizer, if available. The onlyattended parameter indicates whether the function only consider attended appointments.</p>
<h3>Parameters</h3>
```
organizerid int // organizer id
onlyattended int // indicator, whether to only consider attended appointments
```

<h3>Returns</h3>
```
hasappointment int // indicator whether user has an appointment
appointment **Optional** // organizer appointment information
{
	id int // appointment id
	slotid int // slot id
	groupid int // group id (0 if not group organizer)
	attended int // indicator whether user attended the appointment
	grade string // grade received
	feedback string // feedback for the appointment
	comments string // appointment comments
	allownewappointments int // whether re-registration is allowed
}
```

<hr/>
</details>
</td></tr><tr><td><strong>ModPublication</strong></td><td><details>
<summary>mod_publication_get_publications_by_courses</summary>
<br/>
<p>Get all publications for the given courses</p>
<h3>Parameters</h3>
```
courseids // Array of course ids (all enrolled courses if empty array)
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
publications // All publications for the given courses
[
	{
		id int // publication id
		course int // course id the publication belongs to
		name string // publication name
		intro string // intro/description of the publication
		introformat int // intro format
		files **Optional** // files in this publication
		[
			{
				id int // file id
				name string // file name
				mimetype string // file mime type
				download_url string // download url for this file
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_publication_get_publication</summary>
<br/>
<p>Get the publication with the given id</p>
<h3>Parameters</h3>
```
publicationid int // The id of the publication
```

<h3>Returns</h3>
```
publication // publication information
{
	id int // publication id
	course int // course id the publication belongs to
	name string // publication name
	intro string // intro/description of the publication
	introformat int // intro format
	files **Optional** // files in this publication
	[
		{
			id int // file id
			name string // file name
			mimetype string // file mime type
			download_url string // download url for this file
		}
	]
}
```

<hr/>
</details>
</td></tr><tr><td><strong>CoreCalendar</strong></td><td><details>
<summary>core_calendar_create_calendar_events</summary>
<br/>
<p>Create calendar events</p>
<h3>Parameters</h3>
```
events // 
[
	{
		name string // event name
		description string // Description
		format int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		courseid int // course id
		groupid int // group id
		repeats int // number of repeats
		eventtype string // Event type
		timestart int // timestart
		timeduration int // time duration
		visible int // visible
		sequence int // sequence
	}
]
```

<h3>Returns</h3>
```
events // 
[
	{
		id int // event id
		name string // event name
		description string **Optional** // Description
		format int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		courseid int // course id
		groupid int // group id
		userid int // user id
		repeatid int **Optional** // repeat id
		modulename string **Optional** // module name
		instance int // instance id
		eventtype string // Event type
		timestart int // timestart
		timeduration int // time duration
		visible int // visible
		uuid string **Optional** // unique id of ical events
		sequence int // sequence
		timemodified int // time modified
		subscriptionid int **Optional** // Subscription id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_calendar_delete_calendar_events</summary>
<br/>
<p>Delete calendar events</p>
<h3>Parameters</h3>
```
events // 
[
	{
		eventid int // Event ID
		repeat int // Delete comeplete series if repeated event
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_calendar_get_action_events_by_course</summary>
<br/>
<p>Get calendar action events by course</p>
<h3>Parameters</h3>
```
courseid int // Course id
timesortfrom int // Time sort from
timesortto int // Time sort to
aftereventid int // The last seen event id
limitnum int // Limit number
```

<h3>Returns</h3>
```
events // events
[
	{
		id int // id
		name string // name
		description string **Optional** // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string **Optional** // location
		categoryid int **Optional** // categoryid
		groupid int **Optional** // groupid
		userid int **Optional** // userid
		repeatid int **Optional** // repeatid
		eventcount int **Optional** // eventcount
		component string **Optional** // component
		modulename string **Optional** // modulename
		instance int **Optional** // instance
		eventtype string // eventtype
		timestart int // timestart
		timeduration int // timeduration
		timesort int // timesort
		timeusermidnight int // timeusermidnight
		visible int // visible
		timemodified int // timemodified
		icon // 
		{
			key string // key
			component string // component
			alttext string // alttext
		}
		category **Optional** // 
		{
			id int // id
			name string // name
			idnumber string // idnumber
			description string **Optional** // description
			parent int // parent
			coursecount int // coursecount
			visible int // visible
			timemodified int // timemodified
			depth int // depth
			nestedname string // nestedname
			url string // url
		}
		course **Optional** // 
		{
			id int // id
			fullname string // fullname
			shortname string // shortname
			idnumber string // idnumber
			summary string // summary
			summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			startdate int // startdate
			enddate int // enddate
			visible int // visible
			fullnamedisplay string // fullnamedisplay
			viewurl string // viewurl
			courseimage string // courseimage
			progress int **Optional** // progress
			hasprogress int // hasprogress
			isfavourite int // isfavourite
			hidden int // hidden
			timeaccess int **Optional** // timeaccess
			showshortname int // showshortname
			coursecategory string // coursecategory
		}
		subscription **Optional** // 
		{
			displayeventsource int // displayeventsource
			subscriptionname string **Optional** // subscriptionname
			subscriptionurl string **Optional** // subscriptionurl
		}
		canedit int // canedit
		candelete int // candelete
		deleteurl string // deleteurl
		editurl string // editurl
		viewurl string // viewurl
		formattedtime string // formattedtime
		isactionevent int // isactionevent
		iscourseevent int // iscourseevent
		iscategoryevent int // iscategoryevent
		groupname string **Optional** // groupname
		normalisedeventtype string // normalisedeventtype
		normalisedeventtypetext string // normalisedeventtypetext
		action **Optional** // 
		{
			name string // name
			url string // url
			itemcount int // itemcount
			actionable int // actionable
			showitemcount int // showitemcount
		}
		url string // url
	}
]
firstid int // firstid
lastid int // lastid
```

<hr/>
</details>
<details>
<summary>core_calendar_get_action_events_by_courses</summary>
<br/>
<p>Get calendar action events by courses</p>
<h3>Parameters</h3>
```
courseids // 
[
	{
		int // Course id
	}
]
timesortfrom int // Time sort from
timesortto int // Time sort to
limitnum int // Limit number
```

<h3>Returns</h3>
```
groupedbycourse // groupedbycourse
[
	{
		events // events
		[
			{
				id int // id
				name string // name
				description string **Optional** // description
				descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				location string **Optional** // location
				categoryid int **Optional** // categoryid
				groupid int **Optional** // groupid
				userid int **Optional** // userid
				repeatid int **Optional** // repeatid
				eventcount int **Optional** // eventcount
				component string **Optional** // component
				modulename string **Optional** // modulename
				instance int **Optional** // instance
				eventtype string // eventtype
				timestart int // timestart
				timeduration int // timeduration
				timesort int // timesort
				timeusermidnight int // timeusermidnight
				visible int // visible
				timemodified int // timemodified
				icon // 
				{
					key string // key
					component string // component
					alttext string // alttext
				}
				category **Optional** // 
				{
					id int // id
					name string // name
					idnumber string // idnumber
					description string **Optional** // description
					parent int // parent
					coursecount int // coursecount
					visible int // visible
					timemodified int // timemodified
					depth int // depth
					nestedname string // nestedname
					url string // url
				}
				course **Optional** // 
				{
					id int // id
					fullname string // fullname
					shortname string // shortname
					idnumber string // idnumber
					summary string // summary
					summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					startdate int // startdate
					enddate int // enddate
					visible int // visible
					fullnamedisplay string // fullnamedisplay
					viewurl string // viewurl
					courseimage string // courseimage
					progress int **Optional** // progress
					hasprogress int // hasprogress
					isfavourite int // isfavourite
					hidden int // hidden
					timeaccess int **Optional** // timeaccess
					showshortname int // showshortname
					coursecategory string // coursecategory
				}
				subscription **Optional** // 
				{
					displayeventsource int // displayeventsource
					subscriptionname string **Optional** // subscriptionname
					subscriptionurl string **Optional** // subscriptionurl
				}
				canedit int // canedit
				candelete int // candelete
				deleteurl string // deleteurl
				editurl string // editurl
				viewurl string // viewurl
				formattedtime string // formattedtime
				isactionevent int // isactionevent
				iscourseevent int // iscourseevent
				iscategoryevent int // iscategoryevent
				groupname string **Optional** // groupname
				normalisedeventtype string // normalisedeventtype
				normalisedeventtypetext string // normalisedeventtypetext
				action **Optional** // 
				{
					name string // name
					url string // url
					itemcount int // itemcount
					actionable int // actionable
					showitemcount int // showitemcount
				}
				url string // url
			}
		]
		firstid int // firstid
		lastid int // lastid
		courseid int // courseid
	}
]
```

<hr/>
</details>
<details>
<summary>core_calendar_get_action_events_by_timesort</summary>
<br/>
<p>Get calendar action events by tiemsort</p>
<h3>Parameters</h3>
```
timesortfrom int // Time sort from
timesortto int // Time sort to
aftereventid int // The last seen event id
limitnum int // Limit number
limittononsuspendedevents int // Limit the events to courses the user is not suspended in
userid int // The user id
```

<h3>Returns</h3>
```
events // events
[
	{
		id int // id
		name string // name
		description string **Optional** // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string **Optional** // location
		categoryid int **Optional** // categoryid
		groupid int **Optional** // groupid
		userid int **Optional** // userid
		repeatid int **Optional** // repeatid
		eventcount int **Optional** // eventcount
		component string **Optional** // component
		modulename string **Optional** // modulename
		instance int **Optional** // instance
		eventtype string // eventtype
		timestart int // timestart
		timeduration int // timeduration
		timesort int // timesort
		timeusermidnight int // timeusermidnight
		visible int // visible
		timemodified int // timemodified
		icon // 
		{
			key string // key
			component string // component
			alttext string // alttext
		}
		category **Optional** // 
		{
			id int // id
			name string // name
			idnumber string // idnumber
			description string **Optional** // description
			parent int // parent
			coursecount int // coursecount
			visible int // visible
			timemodified int // timemodified
			depth int // depth
			nestedname string // nestedname
			url string // url
		}
		course **Optional** // 
		{
			id int // id
			fullname string // fullname
			shortname string // shortname
			idnumber string // idnumber
			summary string // summary
			summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			startdate int // startdate
			enddate int // enddate
			visible int // visible
			fullnamedisplay string // fullnamedisplay
			viewurl string // viewurl
			courseimage string // courseimage
			progress int **Optional** // progress
			hasprogress int // hasprogress
			isfavourite int // isfavourite
			hidden int // hidden
			timeaccess int **Optional** // timeaccess
			showshortname int // showshortname
			coursecategory string // coursecategory
		}
		subscription **Optional** // 
		{
			displayeventsource int // displayeventsource
			subscriptionname string **Optional** // subscriptionname
			subscriptionurl string **Optional** // subscriptionurl
		}
		canedit int // canedit
		candelete int // candelete
		deleteurl string // deleteurl
		editurl string // editurl
		viewurl string // viewurl
		formattedtime string // formattedtime
		isactionevent int // isactionevent
		iscourseevent int // iscourseevent
		iscategoryevent int // iscategoryevent
		groupname string **Optional** // groupname
		normalisedeventtype string // normalisedeventtype
		normalisedeventtypetext string // normalisedeventtypetext
		action **Optional** // 
		{
			name string // name
			url string // url
			itemcount int // itemcount
			actionable int // actionable
			showitemcount int // showitemcount
		}
		url string // url
	}
]
firstid int // firstid
lastid int // lastid
```

<hr/>
</details>
<details>
<summary>core_calendar_get_calendar_day_view</summary>
<br/>
<p>Fetch the day view data for a calendar</p>
<h3>Parameters</h3>
```
year int // Year to be viewed
month int // Month to be viewed
day int // Day to be viewed
courseid int // Course being viewed
categoryid int // Category being viewed
```

<h3>Returns</h3>
```
events // events
[
	{
		id int // id
		name string // name
		description string **Optional** // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string **Optional** // location
		categoryid int **Optional** // categoryid
		groupid int **Optional** // groupid
		userid int **Optional** // userid
		repeatid int **Optional** // repeatid
		eventcount int **Optional** // eventcount
		component string **Optional** // component
		modulename string **Optional** // modulename
		instance int **Optional** // instance
		eventtype string // eventtype
		timestart int // timestart
		timeduration int // timeduration
		timesort int // timesort
		timeusermidnight int // timeusermidnight
		visible int // visible
		timemodified int // timemodified
		icon // 
		{
			key string // key
			component string // component
			alttext string // alttext
		}
		category **Optional** // 
		{
			id int // id
			name string // name
			idnumber string // idnumber
			description string **Optional** // description
			parent int // parent
			coursecount int // coursecount
			visible int // visible
			timemodified int // timemodified
			depth int // depth
			nestedname string // nestedname
			url string // url
		}
		course **Optional** // 
		{
			id int // id
			fullname string // fullname
			shortname string // shortname
			idnumber string // idnumber
			summary string // summary
			summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			startdate int // startdate
			enddate int // enddate
			visible int // visible
			fullnamedisplay string // fullnamedisplay
			viewurl string // viewurl
			courseimage string // courseimage
			progress int **Optional** // progress
			hasprogress int // hasprogress
			isfavourite int // isfavourite
			hidden int // hidden
			timeaccess int **Optional** // timeaccess
			showshortname int // showshortname
			coursecategory string // coursecategory
		}
		subscription **Optional** // 
		{
			displayeventsource int // displayeventsource
			subscriptionname string **Optional** // subscriptionname
			subscriptionurl string **Optional** // subscriptionurl
		}
		canedit int // canedit
		candelete int // candelete
		deleteurl string // deleteurl
		editurl string // editurl
		viewurl string // viewurl
		formattedtime string // formattedtime
		isactionevent int // isactionevent
		iscourseevent int // iscourseevent
		iscategoryevent int // iscategoryevent
		groupname string **Optional** // groupname
		normalisedeventtype string // normalisedeventtype
		normalisedeventtypetext string // normalisedeventtypetext
		action **Optional** // 
		{
			name string // name
			url string // url
			itemcount int // itemcount
			actionable int // actionable
			showitemcount int // showitemcount
		}
		url string // url
		islastday int // islastday
		popupname string // popupname
		mindaytimestamp int **Optional** // mindaytimestamp
		mindayerror string **Optional** // mindayerror
		maxdaytimestamp int **Optional** // maxdaytimestamp
		maxdayerror string **Optional** // maxdayerror
		draggable int // draggable
	}
]
defaulteventcontext int // defaulteventcontext
filter_selector string // filter_selector
courseid int // courseid
categoryid int **Optional** // categoryid
neweventtimestamp int // neweventtimestamp
date // 
{
	seconds int // seconds
	minutes int // minutes
	hours int // hours
	mday int // mday
	wday int // wday
	mon int // mon
	year int // year
	yday int // yday
	weekday string // weekday
	month string // month
	timestamp int // timestamp
}
periodname string // periodname
previousperiod // 
{
	seconds int // seconds
	minutes int // minutes
	hours int // hours
	mday int // mday
	wday int // wday
	mon int // mon
	year int // year
	yday int // yday
	weekday string // weekday
	month string // month
	timestamp int // timestamp
}
previousperiodlink string // previousperiodlink
previousperiodname string // previousperiodname
nextperiod // 
{
	seconds int // seconds
	minutes int // minutes
	hours int // hours
	mday int // mday
	wday int // wday
	mon int // mon
	year int // year
	yday int // yday
	weekday string // weekday
	month string // month
	timestamp int // timestamp
}
nextperiodname string // nextperiodname
nextperiodlink string // nextperiodlink
larrow string // larrow
rarrow string // rarrow
```

<hr/>
</details>
<details>
<summary>core_calendar_get_calendar_events</summary>
<br/>
<p>Get calendar events</p>
<h3>Parameters</h3>
```
events // Event details
{
	eventids // List of event ids
	[
		{
		int // event ids
		}
	]
	courseids // List of course ids for which events will be returned
	[
		{
		int // course ids
		}
	]
	groupids // List of group ids for which events should be returned
	[
		{
		int // group ids
		}
	]
	categoryids // List of category ids for which events will be returned
	[
		{
		int // Category ids
		}
	]
}
options // Options
{
	userevents int // Set to true to return current user's user events
	siteevents int // Set to true to return site events
	timestart int // Time from which events should be returned
	timeend int // Time to which the events should be returned. We treat 0 and null as no end
	ignorehidden int // Ignore hidden events or not
}
```

<h3>Returns</h3>
```
events // 
[
	{
		id int // event id
		name string // event name
		description string **Optional** // Description
		format int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		courseid int // course id
		categoryid int **Optional** // Category id (only for category events).
		groupid int // group id
		userid int // user id
		repeatid int // repeat id
		modulename string **Optional** // module name
		instance int // instance id
		eventtype string // Event type
		timestart int // timestart
		timeduration int // time duration
		visible int // visible
		uuid string **Optional** // unique id of ical events
		sequence int // sequence
		timemodified int // time modified
		subscriptionid int **Optional** // Subscription id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_calendar_get_calendar_event_by_id</summary>
<br/>
<p>Get calendar event by id</p>
<h3>Parameters</h3>
```
eventid int // The event id to be retrieved
```

<h3>Returns</h3>
```
event // 
{
	id int // id
	name string // name
	description string **Optional** // description
	descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	location string **Optional** // location
	categoryid int **Optional** // categoryid
	groupid int **Optional** // groupid
	userid int **Optional** // userid
	repeatid int **Optional** // repeatid
	eventcount int **Optional** // eventcount
	component string **Optional** // component
	modulename string **Optional** // modulename
	instance int **Optional** // instance
	eventtype string // eventtype
	timestart int // timestart
	timeduration int // timeduration
	timesort int // timesort
	timeusermidnight int // timeusermidnight
	visible int // visible
	timemodified int // timemodified
	icon // 
	{
		key string // key
		component string // component
		alttext string // alttext
	}
	category **Optional** // 
	{
		id int // id
		name string // name
		idnumber string // idnumber
		description string **Optional** // description
		parent int // parent
		coursecount int // coursecount
		visible int // visible
		timemodified int // timemodified
		depth int // depth
		nestedname string // nestedname
		url string // url
	}
	course **Optional** // 
	{
		id int // id
		fullname string // fullname
		shortname string // shortname
		idnumber string // idnumber
		summary string // summary
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		startdate int // startdate
		enddate int // enddate
		visible int // visible
		fullnamedisplay string // fullnamedisplay
		viewurl string // viewurl
		courseimage string // courseimage
		progress int **Optional** // progress
		hasprogress int // hasprogress
		isfavourite int // isfavourite
		hidden int // hidden
		timeaccess int **Optional** // timeaccess
		showshortname int // showshortname
		coursecategory string // coursecategory
	}
	subscription **Optional** // 
	{
		displayeventsource int // displayeventsource
		subscriptionname string **Optional** // subscriptionname
		subscriptionurl string **Optional** // subscriptionurl
	}
	canedit int // canedit
	candelete int // candelete
	deleteurl string // deleteurl
	editurl string // editurl
	viewurl string // viewurl
	formattedtime string // formattedtime
	isactionevent int // isactionevent
	iscourseevent int // iscourseevent
	iscategoryevent int // iscategoryevent
	groupname string **Optional** // groupname
	normalisedeventtype string // normalisedeventtype
	normalisedeventtypetext string // normalisedeventtypetext
	action **Optional** // 
	{
		name string // name
		url string // url
		itemcount int // itemcount
		actionable int // actionable
		showitemcount int // showitemcount
	}
	url string // url
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_calendar_get_calendar_upcoming_view</summary>
<br/>
<p>Fetch the upcoming view data for a calendar</p>
<h3>Parameters</h3>
```
courseid int // Course being viewed
categoryid int // Category being viewed
```

<h3>Returns</h3>
```
events // events
[
	{
		id int // id
		name string // name
		description string **Optional** // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string **Optional** // location
		categoryid int **Optional** // categoryid
		groupid int **Optional** // groupid
		userid int **Optional** // userid
		repeatid int **Optional** // repeatid
		eventcount int **Optional** // eventcount
		component string **Optional** // component
		modulename string **Optional** // modulename
		instance int **Optional** // instance
		eventtype string // eventtype
		timestart int // timestart
		timeduration int // timeduration
		timesort int // timesort
		timeusermidnight int // timeusermidnight
		visible int // visible
		timemodified int // timemodified
		icon // 
		{
			key string // key
			component string // component
			alttext string // alttext
		}
		category **Optional** // 
		{
			id int // id
			name string // name
			idnumber string // idnumber
			description string **Optional** // description
			parent int // parent
			coursecount int // coursecount
			visible int // visible
			timemodified int // timemodified
			depth int // depth
			nestedname string // nestedname
			url string // url
		}
		course **Optional** // 
		{
			id int // id
			fullname string // fullname
			shortname string // shortname
			idnumber string // idnumber
			summary string // summary
			summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			startdate int // startdate
			enddate int // enddate
			visible int // visible
			fullnamedisplay string // fullnamedisplay
			viewurl string // viewurl
			courseimage string // courseimage
			progress int **Optional** // progress
			hasprogress int // hasprogress
			isfavourite int // isfavourite
			hidden int // hidden
			timeaccess int **Optional** // timeaccess
			showshortname int // showshortname
			coursecategory string // coursecategory
		}
		subscription **Optional** // 
		{
			displayeventsource int // displayeventsource
			subscriptionname string **Optional** // subscriptionname
			subscriptionurl string **Optional** // subscriptionurl
		}
		canedit int // canedit
		candelete int // candelete
		deleteurl string // deleteurl
		editurl string // editurl
		viewurl string // viewurl
		formattedtime string // formattedtime
		isactionevent int // isactionevent
		iscourseevent int // iscourseevent
		iscategoryevent int // iscategoryevent
		groupname string **Optional** // groupname
		normalisedeventtype string // normalisedeventtype
		normalisedeventtypetext string // normalisedeventtypetext
		action **Optional** // 
		{
			name string // name
			url string // url
			itemcount int // itemcount
			actionable int // actionable
			showitemcount int // showitemcount
		}
		url string // url
		islastday int // islastday
		popupname string // popupname
		mindaytimestamp int **Optional** // mindaytimestamp
		mindayerror string **Optional** // mindayerror
		maxdaytimestamp int **Optional** // maxdaytimestamp
		maxdayerror string **Optional** // maxdayerror
		draggable int // draggable
	}
]
defaulteventcontext int // defaulteventcontext
filter_selector string // filter_selector
courseid int // courseid
categoryid int **Optional** // categoryid
isloggedin int // isloggedin
date // 
{
	seconds int // seconds
	minutes int // minutes
	hours int // hours
	mday int // mday
	wday int // wday
	mon int // mon
	year int // year
	yday int // yday
	weekday string // weekday
	month string // month
	timestamp int // timestamp
}
```

<hr/>
</details>
<details>
<summary>core_calendar_get_calendar_upcoming_view</summary>
<br/>
<p>Fetch the upcoming view data for a calendar</p>
<h3>Parameters</h3>
```
courseid int // Course being viewed
categoryid int // Category being viewed
```

<h3>Returns</h3>
```
events // events
[
	{
		id int // id
		name string // name
		description string **Optional** // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		location string **Optional** // location
		categoryid int **Optional** // categoryid
		groupid int **Optional** // groupid
		userid int **Optional** // userid
		repeatid int **Optional** // repeatid
		eventcount int **Optional** // eventcount
		component string **Optional** // component
		modulename string **Optional** // modulename
		instance int **Optional** // instance
		eventtype string // eventtype
		timestart int // timestart
		timeduration int // timeduration
		timesort int // timesort
		timeusermidnight int // timeusermidnight
		visible int // visible
		timemodified int // timemodified
		icon // 
		{
			key string // key
			component string // component
			alttext string // alttext
		}
		category **Optional** // 
		{
			id int // id
			name string // name
			idnumber string // idnumber
			description string **Optional** // description
			parent int // parent
			coursecount int // coursecount
			visible int // visible
			timemodified int // timemodified
			depth int // depth
			nestedname string // nestedname
			url string // url
		}
		course **Optional** // 
		{
			id int // id
			fullname string // fullname
			shortname string // shortname
			idnumber string // idnumber
			summary string // summary
			summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			startdate int // startdate
			enddate int // enddate
			visible int // visible
			fullnamedisplay string // fullnamedisplay
			viewurl string // viewurl
			courseimage string // courseimage
			progress int **Optional** // progress
			hasprogress int // hasprogress
			isfavourite int // isfavourite
			hidden int // hidden
			timeaccess int **Optional** // timeaccess
			showshortname int // showshortname
			coursecategory string // coursecategory
		}
		subscription **Optional** // 
		{
			displayeventsource int // displayeventsource
			subscriptionname string **Optional** // subscriptionname
			subscriptionurl string **Optional** // subscriptionurl
		}
		canedit int // canedit
		candelete int // candelete
		deleteurl string // deleteurl
		editurl string // editurl
		viewurl string // viewurl
		formattedtime string // formattedtime
		isactionevent int // isactionevent
		iscourseevent int // iscourseevent
		iscategoryevent int // iscategoryevent
		groupname string **Optional** // groupname
		normalisedeventtype string // normalisedeventtype
		normalisedeventtypetext string // normalisedeventtypetext
		action **Optional** // 
		{
			name string // name
			url string // url
			itemcount int // itemcount
			actionable int // actionable
			showitemcount int // showitemcount
		}
		url string // url
		islastday int // islastday
		popupname string // popupname
		mindaytimestamp int **Optional** // mindaytimestamp
		mindayerror string **Optional** // mindayerror
		maxdaytimestamp int **Optional** // maxdaytimestamp
		maxdayerror string **Optional** // maxdayerror
		draggable int // draggable
	}
]
defaulteventcontext int // defaulteventcontext
filter_selector string // filter_selector
courseid int // courseid
categoryid int **Optional** // categoryid
isloggedin int // isloggedin
date // 
{
	seconds int // seconds
	minutes int // minutes
	hours int // hours
	mday int // mday
	wday int // wday
	mon int // mon
	year int // year
	yday int // yday
	weekday string // weekday
	month string // month
	timestamp int // timestamp
}
```

<hr/>
</details>
<details>
<summary>core_calendar_update_event_start_day</summary>
<br/>
<p>Update the start day (but not time) for an event.</p>
<h3>Parameters</h3>
```
eventid int // Id of event to be updated
daytimestamp int // Timestamp for the new start day
```

<h3>Returns</h3>
```
event // 
{
	id int // id
	name string // name
	description string **Optional** // description
	descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	location string **Optional** // location
	categoryid int **Optional** // categoryid
	groupid int **Optional** // groupid
	userid int **Optional** // userid
	repeatid int **Optional** // repeatid
	eventcount int **Optional** // eventcount
	component string **Optional** // component
	modulename string **Optional** // modulename
	instance int **Optional** // instance
	eventtype string // eventtype
	timestart int // timestart
	timeduration int // timeduration
	timesort int // timesort
	timeusermidnight int // timeusermidnight
	visible int // visible
	timemodified int // timemodified
	icon // 
	{
		key string // key
		component string // component
		alttext string // alttext
	}
	category **Optional** // 
	{
		id int // id
		name string // name
		idnumber string // idnumber
		description string **Optional** // description
		parent int // parent
		coursecount int // coursecount
		visible int // visible
		timemodified int // timemodified
		depth int // depth
		nestedname string // nestedname
		url string // url
	}
	course **Optional** // 
	{
		id int // id
		fullname string // fullname
		shortname string // shortname
		idnumber string // idnumber
		summary string // summary
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		startdate int // startdate
		enddate int // enddate
		visible int // visible
		fullnamedisplay string // fullnamedisplay
		viewurl string // viewurl
		courseimage string // courseimage
		progress int **Optional** // progress
		hasprogress int // hasprogress
		isfavourite int // isfavourite
		hidden int // hidden
		timeaccess int **Optional** // timeaccess
		showshortname int // showshortname
		coursecategory string // coursecategory
	}
	subscription **Optional** // 
	{
		displayeventsource int // displayeventsource
		subscriptionname string **Optional** // subscriptionname
		subscriptionurl string **Optional** // subscriptionurl
	}
	canedit int // canedit
	candelete int // candelete
	deleteurl string // deleteurl
	editurl string // editurl
	viewurl string // viewurl
	formattedtime string // formattedtime
	isactionevent int // isactionevent
	iscourseevent int // iscourseevent
	iscategoryevent int // iscategoryevent
	groupname string **Optional** // groupname
	normalisedeventtype string // normalisedeventtype
	normalisedeventtypetext string // normalisedeventtypetext
	action **Optional** // 
	{
		name string // name
		url string // url
		itemcount int // itemcount
		actionable int // actionable
		showitemcount int // showitemcount
	}
	url string // url
}
```

<hr/>
</details>
</td></tr><tr><td><strong>CoreCourse</strong></td><td><details>
<summary>core_course_get_contents</summary>
<br/>
<p>Get course contents</p>
<h3>Parameters</h3>
```
courseid int // course id
options // Options, used since Moodle 2.9
[
	{
		name string // The expected keys (value format) are:
                                                excludemodules (bool) Do not return modules, return only the sections structure
                                                excludecontents (bool) Do not return module contents (i.e: files inside a resource)
                                                includestealthmodules (bool) Return stealth modules for students in a special
                                                    section (with id -1)
                                                sectionid (int) Return only this section
                                                sectionnumber (int) Return only this section with number (order)
                                                cmid (int) Return only this module information (among the whole sections structure)
                                                modname (string) Return only modules with this name "label, forum, etc..."
                                                modid (int) Return only the module with this id (to be used with modname
		value string // the value of the option,
                                                                    this param is personaly validated in the external function.
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_course_get_courses_by_field</summary>
<br/>
<p>Get courses matching a specific field (id/s, shortname, idnumber, category)</p>
<h3>Parameters</h3>
```
field string // The field to search can be left empty for all courses or:
                    id: course id
                    ids: comma separated course ids
                    shortname: course short name
                    idnumber: course id number
                    category: category id the course belongs to
                
value string // The value to match
```

<h3>Returns</h3>
```
courses // Course
[
	{
		id int // course id
		fullname string // course full name
		displayname string // course display name
		shortname string // course short name
		categoryid int // category id
		categoryname string // category name
		sortorder int **Optional** // Sort order in the category
		summary string // summary
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		summaryfiles **Optional** // summary files in the summary field
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		overviewfiles // additional overview files attached to this course
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		contacts // contact users
		[
			{
				id int // contact user id
				fullname string // contact user fullname
			}
		]
		enrollmentmethods // enrollment methods list
		[
			{
		string // enrollment method
			}
		]
		customfields **Optional** // Custom fields
		[
			{
				name string // The name of the custom field
				shortname string // The shortname of the custom field - to be able to build the field class in the code
				type string // The type of the custom field - text field, checkbox...
				valueraw string // The raw value of the custom field
				value string // The value of the custom field
			}
		]
		idnumber string **Optional** // Id number
		format string **Optional** // Course format: weeks, topics, social, site,..
		showgrades int **Optional** // 1 if grades are shown, otherwise 0
		newsitems int **Optional** // Number of recent items appearing on the course page
		startdate int **Optional** // Timestamp when the course start
		enddate int **Optional** // Timestamp when the course end
		maxbytes int **Optional** // Largest size of file that can be uploaded into
		showreports int **Optional** // Are activity report shown (yes = 1, no =0)
		visible int **Optional** // 1: available to student, 0:not available
		groupmode int **Optional** // no group, separate, visible
		groupmodeforce int **Optional** // 1: yes, 0: no
		defaultgroupingid int **Optional** // default grouping id
		enablecompletion int **Optional** // Completion enabled? 1: yes 0: no
		completionnotify int **Optional** // 1: yes 0: no
		lang string **Optional** // Forced course language
		theme string **Optional** // Fame of the forced theme
		marker int **Optional** // Current course marker
		legacyfiles int **Optional** // If legacy files are enabled
		calendartype string **Optional** // Calendar type
		timecreated int **Optional** // Time when the course was created
		timemodified int **Optional** // Last time  the course was updated
		requested int **Optional** // If is a requested course
		cacherev int **Optional** // Cache revision number
		filters **Optional** // Course filters
		[
			{
				filter string // Filter plugin name
				localstate int // Filter state: 1 for on, -1 for off, 0 if inherit
				inheritedstate int // 1 or 0 to use when localstate is set to inherit
			}
		]
		courseformatoptions **Optional** // Additional options for particular course format.
		[
			{
				name string // Course format option name.
				value string // Course format option value.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_course_get_course_module</summary>
<br/>
<p>Return information about a course module</p>
<h3>Parameters</h3>
```
cmid int // The course module id
```

<h3>Returns</h3>
```
cm // 
{
	id int // The course module id
	course int // The course id
	module int // The module type id
	name string // The activity name
	modname string // The module component name (forum, assign, etc..)
	instance int // The activity instance id
	section int // The module section id
	sectionnum int // The module section number
	groupmode int // Group mode
	groupingid int // Grouping id
	completion int // If completion is enabled
	idnumber string **Optional** // Module id number
	added int **Optional** // Time added
	score int **Optional** // Score
	indent int **Optional** // Indentation
	visible int **Optional** // If visible
	visibleoncoursepage int **Optional** // If visible on course page
	visibleold int **Optional** // Visible old
	completiongradeitemnumber int **Optional** // Completion grade item
	completionview int **Optional** // Completion view setting
	completionexpected int **Optional** // Completion time expected
	showdescription int **Optional** // If the description is showed
	availability string **Optional** // Availability settings
	grade double **Optional** // Grade (max value or scale id)
	scale string **Optional** // Scale items (if used)
	gradepass string **Optional** // Grade to pass (float)
	gradecat int **Optional** // Grade category
	advancedgrading **Optional** // Advanced grading settings
	[
		{
			area string // Gradable area name
			method string // Grading method
		}
	]
	outcomes **Optional** // Outcomes information
	[
		{
			id string // Outcome id
			name string // Outcome full name
			scale string // Scale items
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_course_get_enrolled_courses_by_timeline_classification</summary>
<br/>
<p>List of enrolled courses for the given timeline classification (past, inprogress, or future).</p>
<h3>Parameters</h3>
```
classification string // future, inprogress, or past
limit int // Result set limit
offset int // Result set offset
sort string // Sort string
customfieldname string // Used when classification = customfield
customfieldvalue string // Used when classification = customfield
```

<h3>Returns</h3>
```
courses // Course
[
	{
		id int // id
		fullname string // fullname
		shortname string // shortname
		idnumber string // idnumber
		summary string // summary
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		startdate int // startdate
		enddate int // enddate
		visible int // visible
		fullnamedisplay string // fullnamedisplay
		viewurl string // viewurl
		courseimage string // courseimage
		progress int **Optional** // progress
		hasprogress int // hasprogress
		isfavourite int // isfavourite
		hidden int // hidden
		timeaccess int **Optional** // timeaccess
		showshortname int // showshortname
		coursecategory string // coursecategory
	}
]
nextoffset int // Offset for the next request
```

<hr/>
</details>
<details>
<summary>core_course_search_courses</summary>
<br/>
<p>Search courses by (name, module, block, tag)</p>
<h3>Parameters</h3>
```
criterianame string // criteria name
                                                        (search, modulelist (only admins), blocklist (only admins), tagid)
criteriavalue string // criteria value
page int // page number (0 based)
perpage int // items per page
requiredcapabilities // Optional list of required capabilities (used to filter the list)
[
	{
		string // Capability string used to filter courses by permission
	}
]
limittoenrolled int // limit to enrolled courses
onlywithcompletion int // limit to courses where completion is enabled
```

<h3>Returns</h3>
```
total int // total course count
courses // course
[
	{
		id int // course id
		fullname string // course full name
		displayname string // course display name
		shortname string // course short name
		categoryid int // category id
		categoryname string // category name
		sortorder int **Optional** // Sort order in the category
		summary string // summary
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		summaryfiles **Optional** // summary files in the summary field
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		overviewfiles // additional overview files attached to this course
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		contacts // contact users
		[
			{
				id int // contact user id
				fullname string // contact user fullname
			}
		]
		enrollmentmethods // enrollment methods list
		[
			{
		string // enrollment method
			}
		]
		customfields **Optional** // Custom fields
		[
			{
				name string // The name of the custom field
				shortname string // The shortname of the custom field - to be able to build the field class in the code
				type string // The type of the custom field - text field, checkbox...
				valueraw string // The raw value of the custom field
				value string // The value of the custom field
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>core_course_set_favourite_courses</summary>
<br/>
<p>Add a list of courses to the list of favourite courses.</p>
<h3>Parameters</h3>
```
courses // 
[
	{
		id int // course ID
		favourite int // favourite status
	}
]
```

<h3>Returns</h3>
```
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>Gradereport</strong></td><td><details>
<summary>gradereport_overview_get_course_grades</summary>
<br/>
<p>Get the given user courses final grades</p>
<h3>Parameters</h3>
```
userid int // Get grades for this user (optional, default current)
```

<h3>Returns</h3>
```
grades // 
[
	{
		courseid int // Course id
		grade string // Grade formatted
		rawgrade string // Raw grade, not formatted
		rank int **Optional** // Your rank in the course
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>gradereport_user_get_grades_table</summary>
<br/>
<p>Get the user/s report grades table for a course</p>
<h3>Parameters</h3>
```
courseid int // Course Id
userid int // Return grades only for this user (optional)
groupid int // Get users from this group only
```

<h3>Returns</h3>
```
tables // 
[
	{
		courseid int // course id
		userid int // user id
		userfullname string // user fullname
		maxdepth int // table max depth (needed for printing it)
		tabledata // 
		[
			{
				itemname **Optional** // The item returned data
				{
					class string // class
					colspan int // col span
					content string // cell content
					celltype string // cell type
					id string // id
				}
				leader **Optional** // The item returned data
				{
					class string // class
					rowspan int // row span
				}
				weight **Optional** // weight column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				grade **Optional** // grade column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				range **Optional** // range column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				percentage **Optional** // percentage column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				lettergrade **Optional** // lettergrade column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				rank **Optional** // rank column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				average **Optional** // average column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				feedback **Optional** // feedback column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
				contributiontocoursetotal **Optional** // contributiontocoursetotal column
				{
					class string // class
					content string // cell content
					headers string // headers
				}
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>gradereport_user_get_grade_items</summary>
<br/>
<p>Returns the complete list of grade items for users in a course</p>
<h3>Parameters</h3>
```
courseid int // Course Id
userid int // Return grades only for this user (optional)
groupid int // Get users from this group only
```

<h3>Returns</h3>
```
usergrades // 
[
	{
		courseid int // course id
		userid int // user id
		userfullname string // user fullname
		useridnumber string // user idnumber
		maxdepth int // table max depth (needed for printing it)
		gradeitems // 
		[
			{
				id int // Grade item id
				itemname string // Grade item name
				itemtype string // Grade item type
				itemmodule string // Grade item module
				iteminstance int // Grade item instance
				itemnumber int // Grade item item number
				idnumber string // Grade item idnumber
				categoryid int // Grade item category id
				outcomeid int // Outcome id
				scaleid int // Scale id
				locked int **Optional** // Grade item for user locked?
				cmid int **Optional** // Course module id (if type mod)
				weightraw double **Optional** // Weight raw
				weightformatted string **Optional** // Weight
				status string **Optional** // Status
				graderaw double **Optional** // Grade raw
				gradedatesubmitted int **Optional** // Grade submit date
				gradedategraded int **Optional** // Grade graded date
				gradehiddenbydate int **Optional** // Grade hidden by date?
				gradeneedsupdate int **Optional** // Grade needs update?
				gradeishidden int **Optional** // Grade is hidden?
				gradeislocked int **Optional** // Grade is locked?
				gradeisoverridden int **Optional** // Grade overridden?
				gradeformatted string **Optional** // The grade formatted
				grademin double **Optional** // Grade min
				grademax double **Optional** // Grade max
				rangeformatted string **Optional** // Range formatted
				percentageformatted string **Optional** // Percentage
				lettergradeformatted string **Optional** // Letter grade
				rank int **Optional** // Rank in the course
				numusers int **Optional** // Num users in course
				averageformatted string **Optional** // Grade average
				feedback string **Optional** // Grade feedback
				feedbackformat int **Optional** // feedback format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModAssign</strong></td><td><details>
<summary>mod_assign_get_assignments</summary>
<br/>
<p>Returns the courses and assignments for the users capability</p>
<h3>Parameters</h3>
```
courseids // 0 or more course ids
[
	{
		int // course id, empty for retrieving all the courses where the user is enroled in
	}
]
capabilities // list of capabilities used to filter courses
[
	{
		string // capability
	}
]
includenotenrolledcourses int // whether to return courses that the user can see
                                                                    even if is not enroled in. This requires the parameter courseids
                                                                    to not be empty.
```

<h3>Returns</h3>
```
courses // list of courses
[
	{
		id int // course id
		fullname string // course full name
		shortname string // course short name
		timemodified int // last time modified
		assignments // assignment info
		[
			{
				id int // assignment id
				cmid int // course module id
				course int // course id
				name string // assignment name
				nosubmissions int // no submissions
				submissiondrafts int // submissions drafts
				sendnotifications int // send notifications
				sendlatenotifications int // send notifications
				sendstudentnotifications int // send student notifications (default)
				duedate int // assignment due date
				allowsubmissionsfromdate int // allow submissions from date
				grade int // grade type
				timemodified int // last time assignment was modified
				completionsubmit int // if enabled, set activity as complete following submission
				cutoffdate int // date after which submission is not accepted without an extension
				gradingduedate int // the expected date for marking the submissions
				teamsubmission int // if enabled, students submit as a team
				requireallteammemberssubmit int // if enabled, all team members must submit
				teamsubmissiongroupingid int // the grouping id for the team submission groups
				blindmarking int // if enabled, hide identities until reveal identities actioned
				hidegrader int // If enabled, hide grader to student
				revealidentities int // show identities for a blind marking assignment
				attemptreopenmethod string // method used to control opening new attempts
				maxattempts int // maximum number of attempts allowed
				markingworkflow int // enable marking workflow
				markingallocation int // enable marking allocation
				requiresubmissionstatement int // student must accept submission statement
				preventsubmissionnotingroup int **Optional** // Prevent submission not in group
				submissionstatement string **Optional** // Submission statement formatted.
				submissionstatementformat int **Optional** // submissionstatement format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				configs // configuration settings
				[
					{
						id int **Optional** // assign_plugin_config id
						assignment int **Optional** // assignment id
						plugin string // plugin
						subtype string // subtype
						name string // name
						value string // value
					}
				]
				intro string **Optional** // assignment intro, not allways returned because it deppends on the activity configuration
				introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				introfiles **Optional** // Files in the introduction text
				[
					{
						filename string **Optional** // File name.
						filepath string **Optional** // File path.
						filesize int **Optional** // File size.
						fileurl string **Optional** // Downloadable file url.
						timemodified int **Optional** // Time modified.
						mimetype string **Optional** // File mime type.
						isexternalfile int **Optional** // Whether is an external file.
						repositorytype string **Optional** // The repository type for external files.
					}
				]
				introattachments **Optional** // intro attachments files
				[
					{
						filename string **Optional** // File name.
						filepath string **Optional** // File path.
						filesize int **Optional** // File size.
						fileurl string **Optional** // Downloadable file url.
						timemodified int **Optional** // Time modified.
						mimetype string **Optional** // File mime type.
						isexternalfile int **Optional** // Whether is an external file.
						repositorytype string **Optional** // The repository type for external files.
					}
				]
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item can be 'course' (errorcode 1 or 2) or 'module' (errorcode 1)
		itemid int **Optional** // When item is a course then itemid is a course id. When the item is a module then itemid is a module id
		warningcode string // errorcode can be 1 (no access rights) or 2 (not enrolled or no permissions)
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_assign_get_submission_status</summary>
<br/>
<p>Returns information about an assignment submission status for a given user.</p>
<h3>Parameters</h3>
```
assignid int // assignment instance id
userid int // user id (empty for current user)
groupid int // filter by users in group (used for generating the grading summary).
                    Empty or 0 for all groups information.
```

<h3>Returns</h3>
```
gradingsummary **Optional** // Grading information.
{
	participantcount int // Number of users who can submit.
	submissiondraftscount int // Number of submissions in draft status.
	submissionsenabled int // Whether submissions are enabled or not.
	submissionssubmittedcount int // Number of submissions in submitted status.
	submissionsneedgradingcount int // Number of submissions that need grading.
	warnofungroupedusers string // Whether we need to warn people that there
                                                                        are users without groups ('warningrequired'), warn
                                                                        people there are users who will submit in the default
                                                                        group ('warningoptional') or no warning ('').
}
lastattempt **Optional** // Last attempt information.
{
	submission **Optional** // submission info
	{
		id int // submission id
		userid int // student id
		attemptnumber int // attempt number
		timecreated int // submission creation time
		timemodified int // submission last modified time
		status string // submission status
		groupid int // group id
		assignment int **Optional** // assignment id
		latest int **Optional** // latest attempt
		plugins **Optional** // plugins
		[
			{
				type string // submission plugin type
				name string // submission plugin name
				fileareas **Optional** // fileareas
				[
					{
						area string // file area
						files **Optional** // files
						[
							{
								filename string **Optional** // File name.
								filepath string **Optional** // File path.
								filesize int **Optional** // File size.
								fileurl string **Optional** // Downloadable file url.
								timemodified int **Optional** // Time modified.
								mimetype string **Optional** // File mime type.
								isexternalfile int **Optional** // Whether is an external file.
								repositorytype string **Optional** // The repository type for external files.
							}
						]
					}
				]
				editorfields **Optional** // editorfields
				[
					{
						name string // field name
						description string // field description
						text string // field value
						format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					}
				]
			}
		]
		gradingstatus string **Optional** // Grading status.
	}
	teamsubmission **Optional** // submission info
	{
		id int // submission id
		userid int // student id
		attemptnumber int // attempt number
		timecreated int // submission creation time
		timemodified int // submission last modified time
		status string // submission status
		groupid int // group id
		assignment int **Optional** // assignment id
		latest int **Optional** // latest attempt
		plugins **Optional** // plugins
		[
			{
				type string // submission plugin type
				name string // submission plugin name
				fileareas **Optional** // fileareas
				[
					{
						area string // file area
						files **Optional** // files
						[
							{
								filename string **Optional** // File name.
								filepath string **Optional** // File path.
								filesize int **Optional** // File size.
								fileurl string **Optional** // Downloadable file url.
								timemodified int **Optional** // Time modified.
								mimetype string **Optional** // File mime type.
								isexternalfile int **Optional** // Whether is an external file.
								repositorytype string **Optional** // The repository type for external files.
							}
						]
					}
				]
				editorfields **Optional** // editorfields
				[
					{
						name string // field name
						description string // field description
						text string // field value
						format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					}
				]
			}
		]
		gradingstatus string **Optional** // Grading status.
	}
	submissiongroup int **Optional** // The submission group id (for group submissions only).
	submissiongroupmemberswhoneedtosubmit **Optional** // List of users who still need to submit (for group submissions only).
	[
		{
		int // USER id.
		}
	]
	submissionsenabled int // Whether submissions are enabled or not.
	locked int // Whether new submissions are locked.
	graded int // Whether the submission is graded.
	canedit int // Whether the user can edit the current submission.
	caneditowner int // Whether the owner of the submission can edit it.
	cansubmit int // Whether the user can submit.
	extensionduedate int // Extension due date.
	blindmarking int // Whether blind marking is enabled.
	gradingstatus string // Grading status.
	usergroups // User groups in the course.
	[
		{
		int // Group id.
		}
	]
}
feedback **Optional** // Feedback for the last attempt.
{
	grade **Optional** // grade information
	{
		id int // grade id
		assignment int **Optional** // assignment id
		userid int // student id
		attemptnumber int // attempt number
		timecreated int // grade creation time
		timemodified int // grade last modified time
		grader int // grader, -1 if grader is hidden
		grade string // grade
		gradefordisplay string **Optional** // grade rendered into a format suitable for display
	}
	gradefordisplay string // Grade rendered into a format suitable for display.
	gradeddate int // The date the user was graded.
	plugins **Optional** // Plugins info.
	[
		{
			type string // submission plugin type
			name string // submission plugin name
			fileareas **Optional** // fileareas
			[
				{
					area string // file area
					files **Optional** // files
					[
						{
							filename string **Optional** // File name.
							filepath string **Optional** // File path.
							filesize int **Optional** // File size.
							fileurl string **Optional** // Downloadable file url.
							timemodified int **Optional** // Time modified.
							mimetype string **Optional** // File mime type.
							isexternalfile int **Optional** // Whether is an external file.
							repositorytype string **Optional** // The repository type for external files.
						}
					]
				}
			]
			editorfields **Optional** // editorfields
			[
				{
					name string // field name
					description string // field description
					text string // field value
					format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				}
			]
		}
	]
}
previousattempts **Optional** // List all the previous attempts did by the user.
[
	{
		attemptnumber int // Attempt number.
		submission **Optional** // submission info
		{
			id int // submission id
			userid int // student id
			attemptnumber int // attempt number
			timecreated int // submission creation time
			timemodified int // submission last modified time
			status string // submission status
			groupid int // group id
			assignment int **Optional** // assignment id
			latest int **Optional** // latest attempt
			plugins **Optional** // plugins
			[
				{
					type string // submission plugin type
					name string // submission plugin name
					fileareas **Optional** // fileareas
					[
						{
							area string // file area
							files **Optional** // files
							[
								{
									filename string **Optional** // File name.
									filepath string **Optional** // File path.
									filesize int **Optional** // File size.
									fileurl string **Optional** // Downloadable file url.
									timemodified int **Optional** // Time modified.
									mimetype string **Optional** // File mime type.
									isexternalfile int **Optional** // Whether is an external file.
									repositorytype string **Optional** // The repository type for external files.
								}
							]
						}
					]
					editorfields **Optional** // editorfields
					[
						{
							name string // field name
							description string // field description
							text string // field value
							format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
						}
					]
				}
			]
			gradingstatus string **Optional** // Grading status.
		}
		grade **Optional** // grade information
		{
			id int // grade id
			assignment int **Optional** // assignment id
			userid int // student id
			attemptnumber int // attempt number
			timecreated int // grade creation time
			timemodified int // grade last modified time
			grader int // grader, -1 if grader is hidden
			grade string // grade
			gradefordisplay string **Optional** // grade rendered into a format suitable for display
		}
		feedbackplugins **Optional** // Feedback info.
		[
			{
				type string // submission plugin type
				name string // submission plugin name
				fileareas **Optional** // fileareas
				[
					{
						area string // file area
						files **Optional** // files
						[
							{
								filename string **Optional** // File name.
								filepath string **Optional** // File path.
								filesize int **Optional** // File size.
								fileurl string **Optional** // Downloadable file url.
								timemodified int **Optional** // Time modified.
								mimetype string **Optional** // File mime type.
								isexternalfile int **Optional** // Whether is an external file.
								repositorytype string **Optional** // The repository type for external files.
							}
						]
					}
				]
				editorfields **Optional** // editorfields
				[
					{
						name string // field name
						description string // field description
						text string // field value
						format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					}
				]
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_assign_save_submission</summary>
<br/>
<p>Update the current students submission</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
plugindata // 
{
	onlinetext_editor **Optional** // Editor structure
	{
		text string // The text for this submission.
		format int // The format for this submission
		itemid int // The draft area id for files attached to the submission
	}
	files_filemanager int **Optional** // The id of a draft area containing files for this submission.
}
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_submit_for_grading</summary>
<br/>
<p>Submit the current students assignment for grading</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
acceptsubmissionstatement int // Accept the assignment submission statement
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
</td></tr><tr><td><strong>ModBook</strong></td><td><details>
<summary>mod_book_get_books_by_courses</summary>
<br/>
<p>Returns a list of book instances in a provided set of courses,
                            if no courses are provided then all the book instances the user has access to will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
books // 
[
	{
		id int // Book id
		coursemodule int // Course module id
		course int // Course id
		name string // Book name
		intro string // The Book intro
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		numbering int // Book numbering configuration
		navstyle int // Book navigation style configuration
		customtitles int // Book custom titles type
		revision int **Optional** // Book revision
		timecreated int **Optional** // Time of creation
		timemodified int **Optional** // Time of last modification
		section int **Optional** // Course section id
		visible int **Optional** // Visible
		groupmode int **Optional** // Group mode
		groupingid int **Optional** // Group id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModChoice</strong></td><td><details>
<summary>mod_choice_delete_choice_responses</summary>
<br/>
<p>Delete the given submitted responses in a choice</p>
<h3>Parameters</h3>
```
choiceid int // choice instance id
responses // Array of response ids, empty for deleting all the current user responses.
[
	{
		int // response id
	}
]
```

<h3>Returns</h3>
```
status int // status, true if everything went right
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_choice_get_choices_by_courses</summary>
<br/>
<p>Returns a list of choice instances in a provided set of courses,
                            if no courses are provided then all the choice instances the user has access to will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
choices // 
[
	{
		id int // Choice instance id
		coursemodule int // Course module id
		course int // Course id
		name string // Choice name
		intro string // The choice intro
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		publish int **Optional** // If choice is published
		showresults int **Optional** // 0 never, 1 after answer, 2 after close, 3 always
		display int **Optional** // Display mode (vertical, horizontal)
		allowupdate int **Optional** // Allow update
		allowmultiple int **Optional** // Allow multiple choices
		showunanswered int **Optional** // Show users who not answered yet
		includeinactive int **Optional** // Include inactive users
		limitanswers int **Optional** // Limit unswers
		timeopen int **Optional** // Date of opening validity
		timeclose int **Optional** // Date of closing validity
		showpreview int **Optional** // Show preview before timeopen
		timemodified int **Optional** // Time of last modification
		completionsubmit int **Optional** // Completion on user submission
		showavailable int **Optional** // Show available spaces
		section int **Optional** // Course section id
		visible int **Optional** // Visible
		groupmode int **Optional** // Group mode
		groupingid int **Optional** // Group id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_choice_get_choice_options</summary>
<br/>
<p>Retrieve options for a specific choice.</p>
<h3>Parameters</h3>
```
choiceid int // choice instance id
```

<h3>Returns</h3>
```
options // Options
[
	{
		id int // option id
		text string // text of the choice
		maxanswers int // maximum number of answers
		displaylayout int // true for orizontal, otherwise vertical
		countanswers int // number of answers
		checked int // we already answered
		disabled int // option disabled
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_choice_submit_choice_response</summary>
<br/>
<p>Submit responses to a specific choice item.</p>
<h3>Parameters</h3>
```
choiceid int // choice instance id
responses // Array of response ids
[
	{
		int // answer id
	}
]
```

<h3>Returns</h3>
```
answers // 
[
	{
		id int // answer id
		choiceid int // choiceid
		userid int // user id
		optionid int // optionid
		timemodified int // time of last modification
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModData</strong></td><td><details>
<summary>mod_data_get_databases_by_courses</summary>
<br/>
<p>Returns a list of database instances in a provided set of courses, if
            no courses are provided then all the database instances the user has access to will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
databases // 
[
	{
		id int // Database id
		course int // Course id
		name string // Database name
		intro string // The Database intro
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		comments int // comments enabled
		timeavailablefrom int // timeavailablefrom field
		timeavailableto int // timeavailableto field
		timeviewfrom int // timeviewfrom field
		timeviewto int // timeviewto field
		requiredentries int // requiredentries field
		requiredentriestoview int // requiredentriestoview field
		maxentries int // maxentries field
		rssarticles int // rssarticles field
		singletemplate string // singletemplate field
		listtemplate string // listtemplate field
		listtemplateheader string // listtemplateheader field
		listtemplatefooter string // listtemplatefooter field
		addtemplate string // addtemplate field
		rsstemplate string // rsstemplate field
		rsstitletemplate string // rsstitletemplate field
		csstemplate string // csstemplate field
		jstemplate string // jstemplate field
		asearchtemplate string // asearchtemplate field
		approval int // approval field
		manageapproved int // manageapproved field
		scale int **Optional** // scale field
		assessed int **Optional** // assessed field
		assesstimestart int **Optional** // assesstimestart field
		assesstimefinish int **Optional** // assesstimefinish field
		defaultsort int // defaultsort field
		defaultsortdir int // defaultsortdir field
		editany int **Optional** // editany field (not used any more)
		notification int **Optional** // notification field (not used any more)
		timemodified int **Optional** // Time modified
		coursemodule int // coursemodule
		introfiles **Optional** // introfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_data_get_data_access_information</summary>
<br/>
<p>Return access information for a given database.</p>
<h3>Parameters</h3>
```
databaseid int // Database instance id.
groupid int // Group id, 0 means that the function will determine the user group.
```

<h3>Returns</h3>
```
groupid int // User current group id (calculated)
canaddentry int // Whether the user can add entries or not.
canmanageentries int // Whether the user can manage entries or not.
canapprove int // Whether the user can approve entries or not.
timeavailable int // Whether the database is available or not by time restrictions.
inreadonlyperiod int // Whether the database is in read mode only.
numentries int // The number of entries the current user added.
entrieslefttoadd int // The number of entries left to complete the activity.
entrieslefttoview int // The number of entries left to view other users entries.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_data_get_entries</summary>
<br/>
<p>Return the complete list of entries of the given database.</p>
<h3>Parameters</h3>
```
databaseid int // data instance id
groupid int // Group id, 0 means that the function will determine the user group
returncontents int // Whether to return contents or not. This will return each entry
                                                        raw contents and the complete list view (using the template).
sort int // Sort the records by this field id, reserved ids are:
                                                0: timeadded
                                                -1: firstname
                                                -2: lastname
                                                -3: approved
                                                -4: timemodified.
                                                Empty for using the default database setting.
order string // The direction of the sorting: 'ASC' or 'DESC'.
                                                Empty for using the default database setting.
page int // The page of records to return.
perpage int // The number of records to return per page
```

<h3>Returns</h3>
```
entries // 
[
	{
		id int // Record id.
		userid int // The id of the user who created the record.
		groupid int // The group id this record belongs to (0 for no groups).
		dataid int // The database id this record belongs to.
		timecreated int // Time the record was created.
		timemodified int // Last time the record was modified.
		approved int // Whether the entry has been approved (if the database is configured in that way).
		canmanageentry int // Whether the current user can manage this entry
		fullname string **Optional** // The user who created the entry fullname.
		contents **Optional** // The record contents.
		[
			{
				id int // Content id.
				fieldid int // The field type of the content.
				recordid int // The record this content belongs to.
				content string // Contents.
				content1 string // Contents.
				content2 string // Contents.
				content3 string // Contents.
				content4 string // Contents.
				files **Optional** // files
				[
					{
						filename string **Optional** // File name.
						filepath string **Optional** // File path.
						filesize int **Optional** // File size.
						fileurl string **Optional** // Downloadable file url.
						timemodified int **Optional** // Time modified.
						mimetype string **Optional** // File mime type.
						isexternalfile int **Optional** // Whether is an external file.
						repositorytype string **Optional** // The repository type for the external files.
					}
				]
			}
		]
		tags **Optional** // Tags.
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
totalcount int // Total count of records.
totalfilesize int // Total size (bytes) of the files included in the records.
listviewcontents string **Optional** // The list view contents as is rendered in the site.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_data_get_entry</summary>
<br/>
<p>Return one entry record from the database, including contents optionally.</p>
<h3>Parameters</h3>
```
entryid int // record entry id
returncontents int // Whether to return contents or not.
```

<h3>Returns</h3>
```
entry // 
{
	id int // Record id.
	userid int // The id of the user who created the record.
	groupid int // The group id this record belongs to (0 for no groups).
	dataid int // The database id this record belongs to.
	timecreated int // Time the record was created.
	timemodified int // Last time the record was modified.
	approved int // Whether the entry has been approved (if the database is configured in that way).
	canmanageentry int // Whether the current user can manage this entry
	fullname string **Optional** // The user who created the entry fullname.
	contents **Optional** // The record contents.
	[
		{
			id int // Content id.
			fieldid int // The field type of the content.
			recordid int // The record this content belongs to.
			content string // Contents.
			content1 string // Contents.
			content2 string // Contents.
			content3 string // Contents.
			content4 string // Contents.
			files **Optional** // files
			[
				{
					filename string **Optional** // File name.
					filepath string **Optional** // File path.
					filesize int **Optional** // File size.
					fileurl string **Optional** // Downloadable file url.
					timemodified int **Optional** // Time modified.
					mimetype string **Optional** // File mime type.
					isexternalfile int **Optional** // Whether is an external file.
					repositorytype string **Optional** // The repository type for the external files.
				}
			]
		}
	]
	tags **Optional** // Tags.
	[
		{
			id int // Tag id.
			name string // Tag name.
			rawname string // The raw, unnormalised name for the tag as entered by users.
			isstandard int // Whether this tag is standard.
			tagcollid int // Tag collection id.
			taginstanceid int // Tag instance id.
			taginstancecontextid int // Context the tag instance belongs to.
			itemid int // Id of the record tagged.
			ordering int // Tag ordering.
			flag int // Whether the tag is flagged as inappropriate.
		}
	]
}
entryviewcontents string **Optional** // The entry as is rendered in the site.
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_data_get_fields</summary>
<br/>
<p>Return the list of configured fields for the given database.</p>
<h3>Parameters</h3>
```
databaseid int // Database instance id.
```

<h3>Returns</h3>
```
fields // 
[
	{
		id int // Field id.
		dataid int // The field type of the content.
		type string // The field type.
		name string // The field name.
		description string // The field description.
		required int // Whether is a field required or not.
		param1 string // Field parameters
		param2 string // Field parameters
		param3 string // Field parameters
		param4 string // Field parameters
		param5 string // Field parameters
		param6 string // Field parameters
		param7 string // Field parameters
		param8 string // Field parameters
		param9 string // Field parameters
		param10 string // Field parameters
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_data_search_entries</summary>
<br/>
<p>Search for entries in the given database.</p>
<h3>Parameters</h3>
```
databaseid int // data instance id
groupid int // Group id, 0 means that the function will determine the user group
returncontents int // Whether to return contents or not.
search string // search string (empty when using advanced)
advsearch // Advanced search
[
	{
		name string // Field key for search.
                                                            Use fn or ln for first or last name
		value string // JSON encoded value for search
	}
]
sort int // Sort the records by this field id, reserved ids are:
                                                0: timeadded
                                                -1: firstname
                                                -2: lastname
                                                -3: approved
                                                -4: timemodified.
                                                Empty for using the default database setting.
order string // The direction of the sorting: 'ASC' or 'DESC'.
                                                Empty for using the default database setting.
page int // The page of records to return.
perpage int // The number of records to return per page
```

<h3>Returns</h3>
```
entries // 
[
	{
		id int // Record id.
		userid int // The id of the user who created the record.
		groupid int // The group id this record belongs to (0 for no groups).
		dataid int // The database id this record belongs to.
		timecreated int // Time the record was created.
		timemodified int // Last time the record was modified.
		approved int // Whether the entry has been approved (if the database is configured in that way).
		canmanageentry int // Whether the current user can manage this entry
		fullname string **Optional** // The user who created the entry fullname.
		contents **Optional** // The record contents.
		[
			{
				id int // Content id.
				fieldid int // The field type of the content.
				recordid int // The record this content belongs to.
				content string // Contents.
				content1 string // Contents.
				content2 string // Contents.
				content3 string // Contents.
				content4 string // Contents.
				files **Optional** // files
				[
					{
						filename string **Optional** // File name.
						filepath string **Optional** // File path.
						filesize int **Optional** // File size.
						fileurl string **Optional** // Downloadable file url.
						timemodified int **Optional** // Time modified.
						mimetype string **Optional** // File mime type.
						isexternalfile int **Optional** // Whether is an external file.
						repositorytype string **Optional** // The repository type for the external files.
					}
				]
			}
		]
		tags **Optional** // Tags.
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
totalcount int // Total count of records returned by the search.
maxcount int **Optional** // Total count of records that the user could see in the database
                    (if all the search criterias were removed).
listviewcontents string **Optional** // The list view contents as is rendered in the site.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModFeedback</strong></td><td><details>
<summary>mod_feedback_get_feedbacks_by_courses</summary>
<br/>
<p>Returns a list of feedbacks in a provided list of courses, if no list is provided all feedbacks that
                            the user can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
feedbacks // 
[
	{
		id int // The primary key of the record.
		course int // Course id this feedback is part of.
		name string // Feedback name.
		intro string // Feedback introduction text.
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		anonymous int // Whether the feedback is anonymous.
		email_notification int **Optional** // Whether email notifications will be sent to teachers.
		multiple_submit int // Whether multiple submissions are allowed.
		autonumbering int // Whether questions should be auto-numbered.
		site_after_submit string **Optional** // Link to next page after submission.
		page_after_submit string **Optional** // Text to display after submission.
		page_after_submitformat int // page_after_submit format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		publish_stats int // Whether stats should be published.
		timeopen int **Optional** // Allow answers from this time.
		timeclose int **Optional** // Allow answers until this time.
		timemodified int **Optional** // The time this record was modified.
		completionsubmit int // If this field is set to 1, then the activity will be automatically marked as complete on submission.
		coursemodule int // coursemodule
		introfiles // introfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		pageaftersubmitfiles **Optional** // pageaftersubmitfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_feedback_get_feedback_access_information</summary>
<br/>
<p>Return access information for a given feedback.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id.
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
canviewanalysis int // Whether the user can view the analysis or not.
cancomplete int // Whether the user can complete the feedback or not.
cansubmit int // Whether the user can submit the feedback or not.
candeletesubmissions int // Whether the user can delete submissions or not.
canviewreports int // Whether the user can view the feedback reports or not.
canedititems int // Whether the user can edit feedback items or not.
isempty int // Whether the feedback has questions or not.
isopen int // Whether the feedback has active access time restrictions or not.
isalreadysubmitted int // Whether the feedback is already submitted or not.
isanonymous int // Whether the feedback is anonymous or not.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_feedback_get_finished_responses</summary>
<br/>
<p>Retrieves responses from the last finished attempt.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id.
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
responses // 
[
	{
		id int // The record id.
		course_id int // The course id this record belongs to.
		item int // The item id that was responded.
		completed int // Reference to the feedback_completed table.
		tmp_completed int // Old field - not used anymore.
		value string // The response value.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_feedback_get_items</summary>
<br/>
<p>Returns the items (questions) in the given feedback.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
items // 
[
	{
		id int // The record id.
		feedback int // The feedback instance id this records belongs to.
		template int // If it belogns to a template, the template id.
		name string // The item name.
		label string // The item label.
		presentation string // The text describing the item or the available possible answers.
		typ string // The type of the item.
		hasvalue int // Whether it has a value or not.
		position int // The position in the list of questions.
		required int // Whether is a item (question) required or not.
		dependitem int // The item id this item depend on.
		dependvalue string // The depend value.
		options string // Different additional settings for the item (question).
		itemfiles // itemfiles
		[
			{
				contextid int // contextid
				component string // component
				filearea string // filearea
				itemid int // itemid
				filepath string // filepath
				filename string // filename
				isdir int // isdir
				isimage int // isimage
				timemodified int // timemodified
				timecreated int // timecreated
				filesize int // filesize
				author string // author
				license string // license
				filenameshort string // filenameshort
				filesizeformatted string // filesizeformatted
				icon string // icon
				timecreatedformatted string // timecreatedformatted
				timemodifiedformatted string // timemodifiedformatted
				url string // url
			}
		]
		itemnumber int // The item position number
		otherdata string // Additional data that may be required by external functions
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_feedback_get_last_completed</summary>
<br/>
<p>Retrieves the last completion record for the current user.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
completed // 
{
	id int // The record id.
	feedback int // The feedback instance id this records belongs to.
	userid int // The user who completed the feedback (0 for anonymous).
	timemodified int // The last time the feedback was completed.
	random_response int // The response number (used when shuffling anonymous responses).
	anonymous_response int // Whether is an anonymous response.
	courseid int // The course id where the feedback was completed.
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_feedback_get_page_items</summary>
<br/>
<p>Get a single feedback page items.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
page int // The page to get starting by 0
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
items // 
[
	{
		id int // The record id.
		feedback int // The feedback instance id this records belongs to.
		template int // If it belogns to a template, the template id.
		name string // The item name.
		label string // The item label.
		presentation string // The text describing the item or the available possible answers.
		typ string // The type of the item.
		hasvalue int // Whether it has a value or not.
		position int // The position in the list of questions.
		required int // Whether is a item (question) required or not.
		dependitem int // The item id this item depend on.
		dependvalue string // The depend value.
		options string // Different additional settings for the item (question).
		itemfiles // itemfiles
		[
			{
				contextid int // contextid
				component string // component
				filearea string // filearea
				itemid int // itemid
				filepath string // filepath
				filename string // filename
				isdir int // isdir
				isimage int // isimage
				timemodified int // timemodified
				timecreated int // timecreated
				filesize int // filesize
				author string // author
				license string // license
				filenameshort string // filenameshort
				filesizeformatted string // filesizeformatted
				icon string // icon
				timecreatedformatted string // timecreatedformatted
				timemodifiedformatted string // timemodifiedformatted
				url string // url
			}
		]
		itemnumber int // The item position number
		otherdata string // Additional data that may be required by external functions
	}
]
hasprevpage int // Whether is a previous page.
hasnextpage int // Whether there are more pages.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModFolder</strong></td><td><details>
<summary>mod_folder_get_folders_by_courses</summary>
<br/>
<p>Returns a list of folders in a provided list of courses, if no list is provided all folders that
                            the user can view will be returned. Please note that this WS is not returning the folder contents.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
folders // 
[
	{
		id int // Module id
		coursemodule int // Course module id
		course int // Course id
		name string // Page name
		intro string // Summary
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		revision int // Incremented when after each file changes, to avoid cache
		timemodified int // Last time the folder was modified
		display int // Display type of folder contents on a separate page or inline
		showexpanded int // 1 = expanded, 0 = collapsed for sub-folders
		showdownloadfolder int // Whether to show the download folder button
		section int // Course section id
		visible int // Module visibility
		groupmode int // Group mode
		groupingid int // Grouping id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModForum</strong></td><td><details>
<summary>mod_forum_add_discussion</summary>
<br/>
<p>Add a new discussion into an existing forum.</p>
<h3>Parameters</h3>
```
forumid int // Forum instance ID
subject string // New Discussion subject
message string // New Discussion message (only html format allowed)
groupid int // The group, default to 0
options // Options
[
	{
		name string // The allowed keys (value format) are:
                                        discussionsubscribe (bool); subscribe to the discussion?, default to true
                                        discussionpinned    (bool); is the discussion pinned, default to false
                                        inlineattachmentsid              (int); the draft file area id for inline attachments
                                        attachmentsid       (int); the draft file area id for attachments
                            
		value string // The value of the option,
                                                            This param is validated in the external function.
	}
]
```

<h3>Returns</h3>
```
discussionid int // New Discussion ID
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_add_discussion_post</summary>
<br/>
<p>Create new posts into an existing discussion.</p>
<h3>Parameters</h3>
```
postid int // the post id we are going to reply to
                                                (can be the initial discussion post
subject string // new post subject
message string // new post message (html assumed if messageformat is not provided)
options // Options
[
	{
		name string // The allowed keys (value format) are:
                                        discussionsubscribe (bool); subscribe to the discussion?, default to true
                                        private (bool); make this reply private to the author of the parent post, default to false.
                                        inlineattachmentsid              (int); the draft file area id for inline attachments
                                        attachmentsid       (int); the draft file area id for attachments
                                        topreferredformat (bool); convert the message & messageformat to FORMAT_HTML, defaults to false
                            
		value string // the value of the option,
                                                            this param is validated in the external function.
	}
]
messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
```

<h3>Returns</h3>
```
postid int // new post id
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
post // 
{
	id int // id
	subject string // subject
	replysubject string // replysubject
	message string // message
	messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	author // 
	{
		id int **Optional** // id
		fullname string **Optional** // fullname
		isdeleted int **Optional** // isdeleted
		groups **Optional** // groups
		[
			{
				id int // id
				name string // name
				urls // 
				{
					image string **Optional** // image
				}
			}
		]
		urls // 
		{
			profile string **Optional** // The URL for the use profile page
			profileimage string **Optional** // The URL for the use profile image
		}
	}
	discussionid int // discussionid
	hasparent int // hasparent
	parentid int **Optional** // parentid
	timecreated int // timecreated
	unread int **Optional** // unread
	isdeleted int // isdeleted
	isprivatereply int // isprivatereply
	haswordcount int // haswordcount
	wordcount int **Optional** // wordcount
	charcount int **Optional** // charcount
	capabilities // 
	{
		view int // Whether the user can view the post
		edit int // Whether the user can edit the post
		delete int // Whether the user can delete the post
		split int // Whether the user can split the post
		reply int // Whether the user can reply to the post
		selfenrol int // Whether the user can self enrol into the course
		export int // Whether the user can export the post
		controlreadstatus int // Whether the user can control the read status of the post
		canreplyprivately int // Whether the user can post a private reply
	}
	urls **Optional** // 
	{
		view string **Optional** // The URL used to view the post
		viewisolated string **Optional** // The URL used to view the post in isolation
		viewparent string **Optional** // The URL used to view the parent of the post
		edit string **Optional** // The URL used to edit the post
		delete string **Optional** // The URL used to delete the post
		split string **Optional** // The URL used to split the discussion with the selected post being the first post in the new discussion
		reply string **Optional** // The URL used to reply to the post
		export string **Optional** // The URL used to export the post
		markasread string **Optional** // The URL used to mark the post as read
		markasunread string **Optional** // The URL used to mark the post as unread
		discuss string **Optional** // discuss
	}
	attachments // attachments
	[
		{
			contextid int // contextid
			component string // component
			filearea string // filearea
			itemid int // itemid
			filepath string // filepath
			filename string // filename
			isdir int // isdir
			isimage int // isimage
			timemodified int // timemodified
			timecreated int // timecreated
			filesize int // filesize
			author string // author
			license string // license
			filenameshort string // filenameshort
			filesizeformatted string // filesizeformatted
			icon string // icon
			timecreatedformatted string // timecreatedformatted
			timemodifiedformatted string // timemodifiedformatted
			url string // url
			urls // 
			{
				export string **Optional** // The URL used to export the attachment
			}
			html // 
			{
				plagiarism string **Optional** // The HTML source for the Plagiarism Response
			}
		}
	]
	tags **Optional** // tags
	[
		{
			id int // The ID of the Tag
			tagid int // The tagid
			isstandard int // Whether this is a standard tag
			displayname string // The display name of the tag
			flag int // Wehther this tag is flagged
			urls // 
			{
				view string // The URL to view the tag
			}
		}
	]
	html **Optional** // 
	{
		rating string **Optional** // The HTML source to rate the post
		taglist string **Optional** // The HTML source to view the list of tags
		authorsubheading string **Optional** // The HTML source to view the author details
	}
}
messages **Optional** // list of warnings
[
	{
		type string // The classification to be used in the client side
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_can_add_discussion</summary>
<br/>
<p>Check if the current user can add discussions in the given forum (and optionally for the given group).</p>
<h3>Parameters</h3>
```
forumid int // Forum instance ID
groupid int // The group to check, default to active group.
                                                Use -1 to check if the user can post in all the groups.
```

<h3>Returns</h3>
```
status int // True if the user can add discussions, false otherwise.
canpindiscussions int **Optional** // True if the user can pin discussions, false otherwise.
cancreateattachment int **Optional** // True if the user can add attachments, false otherwise.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_delete_post</summary>
<br/>
<p>Deletes a post or a discussion completely when the post is the discussion topic.</p>
<h3>Parameters</h3>
```
postid int // Post to be deleted. It can be a discussion topic post.
```

<h3>Returns</h3>
```
status int // True if the post/discussion was deleted, false otherwise.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_discussion_post</summary>
<br/>
<p>Get a particular discussion post.</p>
<h3>Parameters</h3>
```
postid int // Post to fetch.
```

<h3>Returns</h3>
```
post // 
{
	id int // id
	subject string // subject
	replysubject string // replysubject
	message string // message
	messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	author // 
	{
		id int **Optional** // id
		fullname string **Optional** // fullname
		isdeleted int **Optional** // isdeleted
		groups **Optional** // groups
		[
			{
				id int // id
				name string // name
				urls // 
				{
					image string **Optional** // image
				}
			}
		]
		urls // 
		{
			profile string **Optional** // The URL for the use profile page
			profileimage string **Optional** // The URL for the use profile image
		}
	}
	discussionid int // discussionid
	hasparent int // hasparent
	parentid int **Optional** // parentid
	timecreated int // timecreated
	unread int **Optional** // unread
	isdeleted int // isdeleted
	isprivatereply int // isprivatereply
	haswordcount int // haswordcount
	wordcount int **Optional** // wordcount
	charcount int **Optional** // charcount
	capabilities // 
	{
		view int // Whether the user can view the post
		edit int // Whether the user can edit the post
		delete int // Whether the user can delete the post
		split int // Whether the user can split the post
		reply int // Whether the user can reply to the post
		selfenrol int // Whether the user can self enrol into the course
		export int // Whether the user can export the post
		controlreadstatus int // Whether the user can control the read status of the post
		canreplyprivately int // Whether the user can post a private reply
	}
	urls **Optional** // 
	{
		view string **Optional** // The URL used to view the post
		viewisolated string **Optional** // The URL used to view the post in isolation
		viewparent string **Optional** // The URL used to view the parent of the post
		edit string **Optional** // The URL used to edit the post
		delete string **Optional** // The URL used to delete the post
		split string **Optional** // The URL used to split the discussion with the selected post being the first post in the new discussion
		reply string **Optional** // The URL used to reply to the post
		export string **Optional** // The URL used to export the post
		markasread string **Optional** // The URL used to mark the post as read
		markasunread string **Optional** // The URL used to mark the post as unread
		discuss string **Optional** // discuss
	}
	attachments // attachments
	[
		{
			contextid int // contextid
			component string // component
			filearea string // filearea
			itemid int // itemid
			filepath string // filepath
			filename string // filename
			isdir int // isdir
			isimage int // isimage
			timemodified int // timemodified
			timecreated int // timecreated
			filesize int // filesize
			author string // author
			license string // license
			filenameshort string // filenameshort
			filesizeformatted string // filesizeformatted
			icon string // icon
			timecreatedformatted string // timecreatedformatted
			timemodifiedformatted string // timemodifiedformatted
			url string // url
			urls // 
			{
				export string **Optional** // The URL used to export the attachment
			}
			html // 
			{
				plagiarism string **Optional** // The HTML source for the Plagiarism Response
			}
		}
	]
	tags **Optional** // tags
	[
		{
			id int // The ID of the Tag
			tagid int // The tagid
			isstandard int // Whether this is a standard tag
			displayname string // The display name of the tag
			flag int // Wehther this tag is flagged
			urls // 
			{
				view string // The URL to view the tag
			}
		}
	]
	html **Optional** // 
	{
		rating string **Optional** // The HTML source to rate the post
		taglist string **Optional** // The HTML source to view the list of tags
		authorsubheading string **Optional** // The HTML source to view the author details
	}
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_discussion_posts</summary>
<br/>
<p>Returns a list of forum posts for a discussion.</p>
<h3>Parameters</h3>
```
discussionid int // The ID of the discussion from which to fetch posts.
sortby string // Sort by this element: id, created or modified
sortdirection string // Sort direction: ASC or DESC
```

<h3>Returns</h3>
```
posts // 
[
	{
		id int // id
		subject string // subject
		replysubject string // replysubject
		message string // message
		messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		author // 
		{
			id int **Optional** // id
			fullname string **Optional** // fullname
			isdeleted int **Optional** // isdeleted
			groups **Optional** // groups
			[
				{
					id int // id
					name string // name
					urls // 
					{
						image string **Optional** // image
					}
				}
			]
			urls // 
			{
				profile string **Optional** // The URL for the use profile page
				profileimage string **Optional** // The URL for the use profile image
			}
		}
		discussionid int // discussionid
		hasparent int // hasparent
		parentid int **Optional** // parentid
		timecreated int // timecreated
		unread int **Optional** // unread
		isdeleted int // isdeleted
		isprivatereply int // isprivatereply
		haswordcount int // haswordcount
		wordcount int **Optional** // wordcount
		charcount int **Optional** // charcount
		capabilities // 
		{
			view int // Whether the user can view the post
			edit int // Whether the user can edit the post
			delete int // Whether the user can delete the post
			split int // Whether the user can split the post
			reply int // Whether the user can reply to the post
			selfenrol int // Whether the user can self enrol into the course
			export int // Whether the user can export the post
			controlreadstatus int // Whether the user can control the read status of the post
			canreplyprivately int // Whether the user can post a private reply
		}
		urls **Optional** // 
		{
			view string **Optional** // The URL used to view the post
			viewisolated string **Optional** // The URL used to view the post in isolation
			viewparent string **Optional** // The URL used to view the parent of the post
			edit string **Optional** // The URL used to edit the post
			delete string **Optional** // The URL used to delete the post
			split string **Optional** // The URL used to split the discussion with the selected post being the first post in the new discussion
			reply string **Optional** // The URL used to reply to the post
			export string **Optional** // The URL used to export the post
			markasread string **Optional** // The URL used to mark the post as read
			markasunread string **Optional** // The URL used to mark the post as unread
			discuss string **Optional** // discuss
		}
		attachments // attachments
		[
			{
				contextid int // contextid
				component string // component
				filearea string // filearea
				itemid int // itemid
				filepath string // filepath
				filename string // filename
				isdir int // isdir
				isimage int // isimage
				timemodified int // timemodified
				timecreated int // timecreated
				filesize int // filesize
				author string // author
				license string // license
				filenameshort string // filenameshort
				filesizeformatted string // filesizeformatted
				icon string // icon
				timecreatedformatted string // timecreatedformatted
				timemodifiedformatted string // timemodifiedformatted
				url string // url
				urls // 
				{
					export string **Optional** // The URL used to export the attachment
				}
				html // 
				{
					plagiarism string **Optional** // The HTML source for the Plagiarism Response
				}
			}
		]
		tags **Optional** // tags
		[
			{
				id int // The ID of the Tag
				tagid int // The tagid
				isstandard int // Whether this is a standard tag
				displayname string // The display name of the tag
				flag int // Wehther this tag is flagged
				urls // 
				{
					view string // The URL to view the tag
				}
			}
		]
		html **Optional** // 
		{
			rating string **Optional** // The HTML source to rate the post
			taglist string **Optional** // The HTML source to view the list of tags
			authorsubheading string **Optional** // The HTML source to view the author details
		}
	}
]
forumid int // The forum id
courseid int // The forum course id
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_discussion_posts</summary>
<br/>
<p>Returns a list of forum posts for a discussion.</p>
<h3>Parameters</h3>
```
discussionid int // The ID of the discussion from which to fetch posts.
sortby string // Sort by this element: id, created or modified
sortdirection string // Sort direction: ASC or DESC
```

<h3>Returns</h3>
```
posts // 
[
	{
		id int // id
		subject string // subject
		replysubject string // replysubject
		message string // message
		messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		author // 
		{
			id int **Optional** // id
			fullname string **Optional** // fullname
			isdeleted int **Optional** // isdeleted
			groups **Optional** // groups
			[
				{
					id int // id
					name string // name
					urls // 
					{
						image string **Optional** // image
					}
				}
			]
			urls // 
			{
				profile string **Optional** // The URL for the use profile page
				profileimage string **Optional** // The URL for the use profile image
			}
		}
		discussionid int // discussionid
		hasparent int // hasparent
		parentid int **Optional** // parentid
		timecreated int // timecreated
		unread int **Optional** // unread
		isdeleted int // isdeleted
		isprivatereply int // isprivatereply
		haswordcount int // haswordcount
		wordcount int **Optional** // wordcount
		charcount int **Optional** // charcount
		capabilities // 
		{
			view int // Whether the user can view the post
			edit int // Whether the user can edit the post
			delete int // Whether the user can delete the post
			split int // Whether the user can split the post
			reply int // Whether the user can reply to the post
			selfenrol int // Whether the user can self enrol into the course
			export int // Whether the user can export the post
			controlreadstatus int // Whether the user can control the read status of the post
			canreplyprivately int // Whether the user can post a private reply
		}
		urls **Optional** // 
		{
			view string **Optional** // The URL used to view the post
			viewisolated string **Optional** // The URL used to view the post in isolation
			viewparent string **Optional** // The URL used to view the parent of the post
			edit string **Optional** // The URL used to edit the post
			delete string **Optional** // The URL used to delete the post
			split string **Optional** // The URL used to split the discussion with the selected post being the first post in the new discussion
			reply string **Optional** // The URL used to reply to the post
			export string **Optional** // The URL used to export the post
			markasread string **Optional** // The URL used to mark the post as read
			markasunread string **Optional** // The URL used to mark the post as unread
			discuss string **Optional** // discuss
		}
		attachments // attachments
		[
			{
				contextid int // contextid
				component string // component
				filearea string // filearea
				itemid int // itemid
				filepath string // filepath
				filename string // filename
				isdir int // isdir
				isimage int // isimage
				timemodified int // timemodified
				timecreated int // timecreated
				filesize int // filesize
				author string // author
				license string // license
				filenameshort string // filenameshort
				filesizeformatted string // filesizeformatted
				icon string // icon
				timecreatedformatted string // timecreatedformatted
				timemodifiedformatted string // timemodifiedformatted
				url string // url
				urls // 
				{
					export string **Optional** // The URL used to export the attachment
				}
				html // 
				{
					plagiarism string **Optional** // The HTML source for the Plagiarism Response
				}
			}
		]
		tags **Optional** // tags
		[
			{
				id int // The ID of the Tag
				tagid int // The tagid
				isstandard int // Whether this is a standard tag
				displayname string // The display name of the tag
				flag int // Wehther this tag is flagged
				urls // 
				{
					view string // The URL to view the tag
				}
			}
		]
		html **Optional** // 
		{
			rating string **Optional** // The HTML source to rate the post
			taglist string **Optional** // The HTML source to view the list of tags
			authorsubheading string **Optional** // The HTML source to view the author details
		}
	}
]
forumid int // The forum id
courseid int // The forum course id
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_forums_by_courses</summary>
<br/>
<p>Returns a list of forum instances in a provided set of courses, if
            no courses are provided then all the forum instances the user has access to will be
            returned.</p>
<h3>Parameters</h3>
```
courseids // Array of Course IDs
[
	{
		int // course ID
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_forum_get_forum_access_information</summary>
<br/>
<p>Return capabilities information for a given forum.</p>
<h3>Parameters</h3>
```
forumid int // Forum instance id.
```

<h3>Returns</h3>
```
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
canaddinstance int **Optional** // Whether the user has the capability mod/forum:addinstance allowed.
canviewdiscussion int **Optional** // Whether the user has the capability mod/forum:viewdiscussion allowed.
canviewhiddentimedposts int **Optional** // Whether the user has the capability mod/forum:viewhiddentimedposts allowed.
canstartdiscussion int **Optional** // Whether the user has the capability mod/forum:startdiscussion allowed.
canreplypost int **Optional** // Whether the user has the capability mod/forum:replypost allowed.
canaddnews int **Optional** // Whether the user has the capability mod/forum:addnews allowed.
canreplynews int **Optional** // Whether the user has the capability mod/forum:replynews allowed.
canviewrating int **Optional** // Whether the user has the capability mod/forum:viewrating allowed.
canviewanyrating int **Optional** // Whether the user has the capability mod/forum:viewanyrating allowed.
canviewallratings int **Optional** // Whether the user has the capability mod/forum:viewallratings allowed.
canrate int **Optional** // Whether the user has the capability mod/forum:rate allowed.
canpostprivatereply int **Optional** // Whether the user has the capability mod/forum:postprivatereply allowed.
canreadprivatereplies int **Optional** // Whether the user has the capability mod/forum:readprivatereplies allowed.
cancreateattachment int **Optional** // Whether the user has the capability mod/forum:createattachment allowed.
candeleteownpost int **Optional** // Whether the user has the capability mod/forum:deleteownpost allowed.
candeleteanypost int **Optional** // Whether the user has the capability mod/forum:deleteanypost allowed.
cansplitdiscussions int **Optional** // Whether the user has the capability mod/forum:splitdiscussions allowed.
canmovediscussions int **Optional** // Whether the user has the capability mod/forum:movediscussions allowed.
canpindiscussions int **Optional** // Whether the user has the capability mod/forum:pindiscussions allowed.
caneditanypost int **Optional** // Whether the user has the capability mod/forum:editanypost allowed.
canviewqandawithoutposting int **Optional** // Whether the user has the capability mod/forum:viewqandawithoutposting allowed.
canviewsubscribers int **Optional** // Whether the user has the capability mod/forum:viewsubscribers allowed.
canmanagesubscriptions int **Optional** // Whether the user has the capability mod/forum:managesubscriptions allowed.
canpostwithoutthrottling int **Optional** // Whether the user has the capability mod/forum:postwithoutthrottling allowed.
canexportdiscussion int **Optional** // Whether the user has the capability mod/forum:exportdiscussion allowed.
canexportforum int **Optional** // Whether the user has the capability mod/forum:exportforum allowed.
canexportpost int **Optional** // Whether the user has the capability mod/forum:exportpost allowed.
canexportownpost int **Optional** // Whether the user has the capability mod/forum:exportownpost allowed.
canaddquestion int **Optional** // Whether the user has the capability mod/forum:addquestion allowed.
canallowforcesubscribe int **Optional** // Whether the user has the capability mod/forum:allowforcesubscribe allowed.
cancanposttomygroups int **Optional** // Whether the user has the capability mod/forum:canposttomygroups allowed.
cancanoverridediscussionlock int **Optional** // Whether the user has the capability mod/forum:canoverridediscussionlock allowed.
cancanoverridecutoff int **Optional** // Whether the user has the capability mod/forum:canoverridecutoff allowed.
cancantogglefavourite int **Optional** // Whether the user has the capability mod/forum:cantogglefavourite allowed.
cangrade int **Optional** // Whether the user has the capability mod/forum:grade allowed.
```

<hr/>
</details>
<details>
<summary>mod_forum_get_forum_discussions</summary>
<br/>
<p>Returns a list of forum discussions optionally sorted and paginated.</p>
<h3>Parameters</h3>
```
forumid int // forum instance id
sortorder int // sort by this element: numreplies, , created or timemodified
page int // current page
perpage int // items per page
groupid int // group id
```

<h3>Returns</h3>
```
discussions // 
[
	{
		id int // Post id
		name string // Discussion name
		groupid int // Group id
		timemodified int // Time modified
		usermodified int // The id of the user who last modified
		timestart int // Time discussion can start
		timeend int // Time discussion ends
		discussion int // Discussion id
		parent int // Parent id
		userid int // User who started the discussion id
		created int // Creation time
		modified int // Time modified
		mailed int // Mailed?
		subject string // The post subject
		message string // The post message
		messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		messagetrust int // Can we trust?
		messageinlinefiles **Optional** // post message inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment string // Has attachments?
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		totalscore int // The post message total score
		mailnow int // Mail now?
		userfullname string // Post author full name
		usermodifiedfullname string // Post modifier full name
		userpictureurl string // Post author picture.
		usermodifiedpictureurl string // Post modifier picture.
		numreplies int // The number of replies in the discussion
		numunread int // The number of unread discussions.
		pinned int // Is the discussion pinned
		locked int // Is the discussion locked
		starred int // Is the discussion starred
		canreply int // Can the user reply to the discussion
		canlock int // Can the user lock the discussion
		canfavourite int // Can the user star the discussion
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_forum_discussions_paginated</summary>
<br/>
<p>** DEPRECATED ** Please do not call this function any more.
                          Returns a list of forum discussions optionally sorted and paginated.</p>
<h3>Parameters</h3>
```
forumid int // forum instance id
sortby string // sort by this element: id, timemodified, timestart or timeend
sortdirection string // sort direction: ASC or DESC
page int // current page
perpage int // items per page
```

<h3>Returns</h3>
```
discussions // 
[
	{
		id int // Post id
		name string // Discussion name
		groupid int // Group id
		timemodified int // Time modified
		usermodified int // The id of the user who last modified
		timestart int // Time discussion can start
		timeend int // Time discussion ends
		discussion int // Discussion id
		parent int // Parent id
		userid int // User who started the discussion id
		created int // Creation time
		modified int // Time modified
		mailed int // Mailed?
		subject string // The post subject
		message string // The post message
		messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		messagetrust int // Can we trust?
		messageinlinefiles **Optional** // post message inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment string // Has attachments?
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		totalscore int // The post message total score
		mailnow int // Mail now?
		userfullname string // Post author full name
		usermodifiedfullname string // Post modifier full name
		userpictureurl string // Post author picture.
		usermodifiedpictureurl string // Post modifier picture.
		numreplies int // The number of replies in the discussion
		numunread int // The number of unread discussions.
		pinned int // Is the discussion pinned
		locked int // Is the discussion locked
		canreply int // Can the user reply to the discussion
		canlock int // Can the user lock the discussion
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_get_forum_discussion_posts</summary>
<br/>
<p>Returns a list of forum posts for a discussion.</p>
<h3>Parameters</h3>
```
discussionid int // discussion ID
sortby string // sort by this element: id, created or modified
sortdirection string // sort direction: ASC or DESC
```

<h3>Returns</h3>
```
posts // 
[
	{
		id int // Post id
		discussion int // Discussion id
		parent int // Parent id
		userid int // User id
		created int // Creation time
		modified int // Time modified
		mailed int // Mailed?
		subject string // The post subject
		message string // The post message
		messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		messagetrust int // Can we trust?
		messageinlinefiles **Optional** // post message inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment string // Has attachments?
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		totalscore int // The post message total score
		mailnow int // Mail now?
		children // 
		[
			{
		int // children post id
			}
		]
		canreply int // The user can reply to posts?
		postread int // The post was read
		userfullname string // Post author full name
		userpictureurl string **Optional** // Post author picture.
		deleted int // This post has been removed.
		isprivatereply int // The post is a private reply
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_forum_set_subscription_state</summary>
<br/>
<p>Set the subscription state</p>
<h3>Parameters</h3>
```
forumid int // Forum that the discussion is in
discussionid int // The discussion to subscribe or unsubscribe
targetstate int // The target state
```

<h3>Returns</h3>
```
id int // id
forumid int // forumid
pinned int // pinned
locked int // locked
istimelocked int // istimelocked
name string // name
firstpostid int // firstpostid
group **Optional** // 
{
	name string // name
	urls // 
	{
		picture string **Optional** // picture
		userlist string **Optional** // userlist
	}
}
times // 
{
	modified int // modified
	start int // start
	end int // end
	locked int // locked
}
userstate // 
{
	subscribed int // subscribed
	favourited int // favourited
}
capabilities // 
{
	subscribe int // subscribe
	move int // move
	pin int // pin
	post int // post
	manage int // manage
	favourite int // favourite
}
urls // 
{
	view string // view
	viewlatest string **Optional** // viewlatest
	viewfirstunread string **Optional** // viewfirstunread
	markasread string // markasread
	subscribe string // subscribe
	pin string **Optional** // pin
}
timed // 
{
	istimed int **Optional** // istimed
	visible int **Optional** // visible
}
```

<hr/>
</details>
<details>
<summary>mod_forum_toggle_favourite_state</summary>
<br/>
<p>Toggle the favourite state</p>
<h3>Parameters</h3>
```
discussionid int // The discussion to subscribe or unsubscribe
targetstate int // The target state
```

<h3>Returns</h3>
```
id int // id
forumid int // forumid
pinned int // pinned
locked int // locked
istimelocked int // istimelocked
name string // name
firstpostid int // firstpostid
group **Optional** // 
{
	name string // name
	urls // 
	{
		picture string **Optional** // picture
		userlist string **Optional** // userlist
	}
}
times // 
{
	modified int // modified
	start int // start
	end int // end
	locked int // locked
}
userstate // 
{
	subscribed int // subscribed
	favourited int // favourited
}
capabilities // 
{
	subscribe int // subscribe
	move int // move
	pin int // pin
	post int // post
	manage int // manage
	favourite int // favourite
}
urls // 
{
	view string // view
	viewlatest string **Optional** // viewlatest
	viewfirstunread string **Optional** // viewfirstunread
	markasread string // markasread
	subscribe string // subscribe
	pin string **Optional** // pin
}
timed // 
{
	istimed int **Optional** // istimed
	visible int **Optional** // visible
}
```

<hr/>
</details>
</td></tr><tr><td><strong>ModGlossary</strong></td><td><details>
<summary>mod_glossary_get_authors</summary>
<br/>
<p>Get the authors.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes self even if all of their entries require approval. When true, also includes authors only having entries pending approval.
}
```

<h3>Returns</h3>
```
count int // The total number of records.
authors // 
[
	{
		id int // The user ID
		fullname string // The fullname
		pictureurl string // The picture URL
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_categories</summary>
<br/>
<p>Get the categories.</p>
<h3>Parameters</h3>
```
id int // The glossary ID
from int // Start returning records from here
limit int // Number of records to return
```

<h3>Returns</h3>
```
count int // The total number of records.
categories // 
[
	{
		id int // The category ID
		glossaryid int // The glossary ID
		name string // The name of the category
		usedynalink int // Whether the category is automatically linked
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_author</summary>
<br/>
<p>Browse entries by author.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
letter string // First letter of firstname or lastname, or either keywords: 'ALL' or 'SPECIAL'.
field string // Search and order using: 'FIRSTNAME' or 'LASTNAME'
sort string // The direction of the order: 'ASC' or 'DESC'
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_author_id</summary>
<br/>
<p>Browse entries by author ID.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
authorid int // The author ID
order string // Order by: 'CONCEPT', 'CREATION' or 'UPDATE'
sort string // The direction of the order: 'ASC' or 'DESC'
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_category</summary>
<br/>
<p>Browse entries by category.</p>
<h3>Parameters</h3>
```
id int // The glossary ID.
categoryid int // The category ID. Use '0' for all categories, or '-1' for uncategorised entries.
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
		categoryid int // The category ID. This may be '-1' when the entry is not categorised
		categoryname string // The category name. May be empty when the entry is not categorised, or the request was limited to one category.
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_date</summary>
<br/>
<p>Browse entries by date.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
order string // Order the records by: 'CREATION' or 'UPDATE'.
sort string // The direction of the order: 'ASC' or 'DESC'
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_letter</summary>
<br/>
<p>Browse entries by letter.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
letter string // A letter, or either keywords: 'ALL' or 'SPECIAL'.
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_search</summary>
<br/>
<p>Browse entries by search query.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
query string // The query string
fullsearch int // The query
order string // Order by: 'CONCEPT', 'CREATION' or 'UPDATE'
sort string // The direction of the order: 'ASC' or 'DESC'
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entries_by_term</summary>
<br/>
<p>Browse entries by term (concept or alias).</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
term string // The entry concept, or alias
from int // Start returning records from here
limit int // Number of records to return
options // An array of options
{
	includenotapproved int // When false, includes the non-approved entries created by the user. When true, also includes the ones that the user has the permission to approve.
}
```

<h3>Returns</h3>
```
count int // The total number of records matching the request.
entries // 
[
	{
		id int // The entry ID
		glossaryid int // The glossary ID
		userid int // Author ID
		userfullname string // Author full name
		userpictureurl string // Author picture
		concept string // The concept
		definition string // The definition
		definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		definitiontrust int // The definition trust flag
		definitioninlinefiles **Optional** // entry definition inline files
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		attachment int // Whether or not the entry has attachments
		attachments **Optional** // attachments
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int // Time created
		timemodified int // Time modified
		teacherentry int // The entry was created by a teacher, or equivalent.
		sourceglossaryid int // The source glossary ID
		usedynalink int // Whether the concept should be automatically linked
		casesensitive int // When true, the matching is case sensitive
		fullmatch int // When true, the matching is done on full words only
		approved int // Whether the entry was approved
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_entry_by_id</summary>
<br/>
<p>Get an entry by ID</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
```

<h3>Returns</h3>
```
entry // 
{
	id int // The entry ID
	glossaryid int // The glossary ID
	userid int // Author ID
	userfullname string // Author full name
	userpictureurl string // Author picture
	concept string // The concept
	definition string // The definition
	definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	definitiontrust int // The definition trust flag
	definitioninlinefiles **Optional** // entry definition inline files
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for external files.
		}
	]
	attachment int // Whether or not the entry has attachments
	attachments **Optional** // attachments
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for external files.
		}
	]
	timecreated int // Time created
	timemodified int // Time modified
	teacherentry int // The entry was created by a teacher, or equivalent.
	sourceglossaryid int // The source glossary ID
	usedynalink int // Whether the concept should be automatically linked
	casesensitive int // When true, the matching is case sensitive
	fullmatch int // When true, the matching is done on full words only
	approved int // Whether the entry was approved
	tags **Optional** // Tags
	[
		{
			id int // Tag id.
			name string // Tag name.
			rawname string // The raw, unnormalised name for the tag as entered by users.
			isstandard int // Whether this tag is standard.
			tagcollid int // Tag collection id.
			taginstanceid int // Tag instance id.
			taginstancecontextid int // Context the tag instance belongs to.
			itemid int // Id of the record tagged.
			ordering int // Tag ordering.
			flag int // Whether the tag is flagged as inappropriate.
		}
	]
}
ratinginfo **Optional** // Rating information
{
	contextid int // Context id.
	component string // Context name.
	ratingarea string // Rating area name.
	canviewall int **Optional** // Whether the user can view all the individual ratings.
	canviewany int **Optional** // Whether the user can view aggregate of ratings of others.
	scales **Optional** // Different scales used information
	[
		{
			id int // Scale id.
			courseid int **Optional** // Course id.
			name string **Optional** // Scale name (when a real scale is used).
			max int // Max value for the scale.
			isnumeric int // Whether is a numeric scale.
			items **Optional** // Scale items. Only returned for not numerical scales.
			[
				{
					value int // Scale value/option id.
					name string // Scale name.
				}
			]
		}
	]
	ratings **Optional** // The ratings
	[
		{
			itemid int // Item id.
			scaleid int **Optional** // Scale id.
			userid int **Optional** // User who rated id.
			aggregate double **Optional** // Aggregated ratings grade.
			aggregatestr string **Optional** // Aggregated ratings as string.
			aggregatelabel string **Optional** // The aggregation label.
			count int **Optional** // Ratings count (used when aggregating).
			rating int **Optional** // The rating the user gave.
			canrate int **Optional** // Whether the user can rate the item.
			canviewaggregate int **Optional** // Whether the user can view the aggregated grade.
		}
	]
}
permissions **Optional** // User permissions for the managing the entry.
{
	candelete int // Whether the user can delete the entry.
	canupdate int // Whether the user can update the entry.
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_glossary_get_glossaries_by_courses</summary>
<br/>
<p>Retrieve a list of glossaries from several courses.</p>
<h3>Parameters</h3>
```
courseids // Array of course IDs
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
glossaries // 
[
	{
		id int // Glossary id
		coursemodule int // Course module id
		course int // Course id
		name string // Glossary name
		intro string // The Glossary intro
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		allowduplicatedentries int // If enabled, multiple entries can have the same concept name
		displayformat string // Display format type
		mainglossary int // If enabled this glossary is a main glossary.
		showspecial int // If enabled, participants can browse the glossary by special characters, such as @ and #
		showalphabet int // If enabled, participants can browse the glossary by letters of the alphabet
		showall int // If enabled, participants can browse all entries at once
		allowcomments int // If enabled, all participants with permission to create comments will be able to add comments to glossary entries
		allowprintview int // If enabled, students are provided with a link to a printer-friendly version of the glossary. The link is always available to teachers
		usedynalink int // If site-wide glossary auto-linking has been enabled by an administrator and this checkbox is ticked, the entry will be automatically linked wherever the concept words and phrases appear throughout the rest of the course.
		defaultapproval int // If set to no, entries require approving by a teacher before they are viewable by everyone.
		approvaldisplayformat string // When approving glossary items you may wish to use a different display format
		globalglossary int // 
		entbypage int // Entries shown per page
		editalways int // Always allow editing
		rsstype int // To enable the RSS feed for this activity, select either concepts with author or concepts without author to be included in the feed
		rssarticles int // This setting specifies the number of glossary entry concepts to include in the RSS feed. Between 5 and 20 generally acceptable
		assessed int // Aggregate type
		assesstimestart int // Restrict rating to items created after this
		assesstimefinish int // Restrict rating to items created before this
		scale int // Scale ID
		timecreated int // Time created
		timemodified int // Time modified
		completionentries int // Number of entries to complete
		section int // Section
		visible int // Visible
		groupmode int // Group mode
		groupingid int // Grouping ID
		browsemodes // 
		[
			{
		string // Modes of browsing allowed
			}
		]
		canaddentry int **Optional** // Whether the user can add a new entry
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModLesson</strong></td><td><details>
<summary>mod_lesson_get_lesson</summary>
<br/>
<p>Return information of a given lesson.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
password string // lesson password
```

<h3>Returns</h3>
```
lesson // 
{
	id int // Standard Moodle primary key.
	course int // Foreign key reference to the course this lesson is part of.
	coursemodule int // Course module id.
	name string // Lesson name.
	intro string **Optional** // Lesson introduction text.
	introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	practice int **Optional** // Practice lesson?
	modattempts int **Optional** // Allow student review?
	usepassword int **Optional** // Password protected lesson?
	password string **Optional** // Password
	dependency int **Optional** // Dependent on (another lesson id)
	conditions string **Optional** // Conditions to enable the lesson
	grade int **Optional** // The total that the grade is scaled to be out of
	custom int **Optional** // Custom scoring?
	ongoing int **Optional** // Display ongoing score?
	usemaxgrade int **Optional** // How to calculate the final grade
	maxanswers int **Optional** // Maximum answers per page
	maxattempts int **Optional** // Maximum attempts
	review int **Optional** // Provide option to try a question again
	nextpagedefault int **Optional** // Action for a correct answer
	feedback int **Optional** // Display default feedback
	minquestions int **Optional** // Minimum number of questions
	maxpages int **Optional** // Number of pages to show
	timelimit int **Optional** // Time limit
	retake int **Optional** // Re-takes allowed
	activitylink int **Optional** // Id of the next activity to be linked once the lesson is completed
	mediafile string **Optional** // Local file path or full external URL
	mediaheight int **Optional** // Popup for media file height
	mediawidth int **Optional** // Popup for media with
	mediaclose int **Optional** // Display a close button in the popup?
	slideshow int **Optional** // Display lesson as slideshow
	width int **Optional** // Slideshow width
	height int **Optional** // Slideshow height
	bgcolor string **Optional** // Slideshow bgcolor
	displayleft int **Optional** // Display left pages menu?
	displayleftif int **Optional** // Minimum grade to display menu
	progressbar int **Optional** // Display progress bar?
	available int **Optional** // Available from
	deadline int **Optional** // Available until
	timemodified int **Optional** // Last time settings were updated
	completionendreached int **Optional** // Require end reached for completion?
	completiontimespent int **Optional** // Student must do this activity at least for
	allowofflineattempts int // Whether to allow the lesson to be attempted offline in the mobile app
	introfiles **Optional** // introfiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
	mediafiles **Optional** // mediafiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_lessons_by_courses</summary>
<br/>
<p>Returns a list of lessons in a provided list of courses,
                            if no list is provided all lessons that the user can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
lessons // 
[
	{
		id int // Standard Moodle primary key.
		course int // Foreign key reference to the course this lesson is part of.
		coursemodule int // Course module id.
		name string // Lesson name.
		intro string **Optional** // Lesson introduction text.
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		practice int **Optional** // Practice lesson?
		modattempts int **Optional** // Allow student review?
		usepassword int **Optional** // Password protected lesson?
		password string **Optional** // Password
		dependency int **Optional** // Dependent on (another lesson id)
		conditions string **Optional** // Conditions to enable the lesson
		grade int **Optional** // The total that the grade is scaled to be out of
		custom int **Optional** // Custom scoring?
		ongoing int **Optional** // Display ongoing score?
		usemaxgrade int **Optional** // How to calculate the final grade
		maxanswers int **Optional** // Maximum answers per page
		maxattempts int **Optional** // Maximum attempts
		review int **Optional** // Provide option to try a question again
		nextpagedefault int **Optional** // Action for a correct answer
		feedback int **Optional** // Display default feedback
		minquestions int **Optional** // Minimum number of questions
		maxpages int **Optional** // Number of pages to show
		timelimit int **Optional** // Time limit
		retake int **Optional** // Re-takes allowed
		activitylink int **Optional** // Id of the next activity to be linked once the lesson is completed
		mediafile string **Optional** // Local file path or full external URL
		mediaheight int **Optional** // Popup for media file height
		mediawidth int **Optional** // Popup for media with
		mediaclose int **Optional** // Display a close button in the popup?
		slideshow int **Optional** // Display lesson as slideshow
		width int **Optional** // Slideshow width
		height int **Optional** // Slideshow height
		bgcolor string **Optional** // Slideshow bgcolor
		displayleft int **Optional** // Display left pages menu?
		displayleftif int **Optional** // Minimum grade to display menu
		progressbar int **Optional** // Display progress bar?
		available int **Optional** // Available from
		deadline int **Optional** // Available until
		timemodified int **Optional** // Last time settings were updated
		completionendreached int **Optional** // Require end reached for completion?
		completiontimespent int **Optional** // Student must do this activity at least for
		allowofflineattempts int // Whether to allow the lesson to be attempted offline in the mobile app
		introfiles **Optional** // introfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		mediafiles **Optional** // mediafiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_lesson_access_information</summary>
<br/>
<p>Return access information for a given lesson.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
```

<h3>Returns</h3>
```
canmanage int // Whether the user can manage the lesson or not.
cangrade int // Whether the user can grade the lesson or not.
canviewreports int // Whether the user can view the lesson reports or not.
reviewmode int // Whether the lesson is in review mode for the current user.
attemptscount int // The number of attempts done by the user.
lastpageseen int // The last page seen id.
leftduringtimedsession int // Whether the user left during a timed session.
firstpageid int // The lesson first page id.
preventaccessreasons // 
[
	{
		reason string // Reason lang string code
		data string // Additional data
		message string // Complete html message
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_pages</summary>
<br/>
<p>Return the list of pages in a lesson (based on the user permissions).</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
password string // optional password (the lesson may be protected)
```

<h3>Returns</h3>
```
pages // 
[
	{
		page // Page fields
		{
			id int // The id of this lesson page
			lessonid int // The id of the lesson this page belongs to
			prevpageid int // The id of the page before this one
			nextpageid int // The id of the next page in the page sequence
			qtype int // Identifies the page type of this page
			qoption int // Used to record page type specific options
			layout int // Used to record page specific layout selections
			display int // Used to record page specific display selections
			timecreated int // Timestamp for when the page was created
			timemodified int // Timestamp for when the page was last modified
			title string **Optional** // The title of this page
			contents string **Optional** // The contents of this page
			contentsformat int **Optional** // contents format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			displayinmenublock int // Toggles display in the left menu block
			type int // The type of the page [question | structure]
			typeid int // The unique identifier for the page type
			typestring string // The string that describes this page type
		}
		answerids // List of answers ids (empty for content pages in  Moodle 1.9)
		[
			{
		int // Answer id
			}
		]
		jumps // List of possible page jumps
		[
			{
		int // Page to jump id
			}
		]
		filescount int // The total number of files attached to the page
		filessizetotal int // The total size of the files
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_page_data</summary>
<br/>
<p>Return information of a given page, including its contents.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
pageid int // the page id
password string // optional password (the lesson may be protected)
review int // if we want to review just after finishing (1 hour margin)
returncontents int // if we must return the complete page contents once rendered
```

<h3>Returns</h3>
```
page **Optional** // Page fields
{
	id int // The id of this lesson page
	lessonid int // The id of the lesson this page belongs to
	prevpageid int // The id of the page before this one
	nextpageid int // The id of the next page in the page sequence
	qtype int // Identifies the page type of this page
	qoption int // Used to record page type specific options
	layout int // Used to record page specific layout selections
	display int // Used to record page specific display selections
	timecreated int // Timestamp for when the page was created
	timemodified int // Timestamp for when the page was last modified
	title string **Optional** // The title of this page
	contents string **Optional** // The contents of this page
	contentsformat int **Optional** // contents format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	displayinmenublock int // Toggles display in the left menu block
	type int // The type of the page [question | structure]
	typeid int // The unique identifier for the page type
	typestring string // The string that describes this page type
}
newpageid int // New page id (if a jump was made)
pagecontent string **Optional** // Page html content
ongoingscore string // The ongoing score message
progress int // Progress percentage in the lesson
contentfiles // List of files.
[
	{
		filename string **Optional** // File name.
		filepath string **Optional** // File path.
		filesize int **Optional** // File size.
		fileurl string **Optional** // Downloadable file url.
		timemodified int **Optional** // Time modified.
		mimetype string **Optional** // File mime type.
		isexternalfile int **Optional** // Whether is an external file.
		repositorytype string **Optional** // The repository type for external files.
	}
]
answers // 
[
	{
		id int // The ID of this answer in the database
		answerfiles // List of files.
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		responsefiles // List of files.
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		jumpto int **Optional** // Identifies where the user goes upon completing a page with this answer
		grade int **Optional** // The grade this answer is worth
		score int **Optional** // The score this answer will give
		flags int **Optional** // Used to store options for the answer
		timecreated int **Optional** // A timestamp of when the answer was created
		timemodified int **Optional** // A timestamp of when the answer was modified
		answer string **Optional** // Possible answer text
		answerformat int **Optional** // answer format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		response string **Optional** // Response text for the answer
		responseformat int **Optional** // response format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	}
]
messages // 
[
	{
		message string // Message.
		type string // Message type: usually a CSS identifier like:
                                success, info, warning, error, notifyproblem, notifyerror, notifytiny, notifysuccess
	}
]
displaymenu int // Whether we should display the menu or not in this page.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_questions_attempts</summary>
<br/>
<p>Return the list of questions attempts in a given lesson.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
attempt int // lesson attempt number
correct int // only fetch correct attempts
pageid int // only fetch attempts at the given page
userid int // only fetch attempts of the given user
```

<h3>Returns</h3>
```
attempts // 
[
	{
		id int // The attempt id
		lessonid int // The attempt lessonid
		pageid int // The attempt pageid
		userid int // The user who did the attempt
		answerid int // The attempt answerid
		retry int // The lesson attempt number
		correct int // If it was the correct answer
		useranswer string // The complete user answer
		timeseen int // The time the question was seen
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_user_attempt</summary>
<br/>
<p>Return information about the given user attempt (including answers).</p>
<h3>Parameters</h3>
```
lessonid int // Lesson instance id.
userid int // The user id. 0 for current user.
lessonattempt int // The attempt number.
```

<h3>Returns</h3>
```
answerpages // 
[
	{
		page **Optional** // Page fields
		{
			id int // The id of this lesson page
			lessonid int // The id of the lesson this page belongs to
			prevpageid int // The id of the page before this one
			nextpageid int // The id of the next page in the page sequence
			qtype int // Identifies the page type of this page
			qoption int // Used to record page type specific options
			layout int // Used to record page specific layout selections
			display int // Used to record page specific display selections
			timecreated int // Timestamp for when the page was created
			timemodified int // Timestamp for when the page was last modified
			title string **Optional** // The title of this page
			contents string **Optional** // The contents of this page
			contentsformat int **Optional** // contents format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			displayinmenublock int // Toggles display in the left menu block
			type int // The type of the page [question | structure]
			typeid int // The unique identifier for the page type
			typestring string // The string that describes this page type
		}
		title string // Page title.
		contents string // Page contents.
		qtype string // Identifies the page type of this page.
		grayout int // If is required to apply a grayout.
		answerdata **Optional** // Answer data (empty in content pages created in Moodle 1.x).
		{
			score string // The score (text version).
			response string // The response text.
			responseformat int // response. format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			answers **Optional** // User answers
			[
				{
		<br />
<b>Notice</b>:  Undefined property: external_multiple_structure::$type in <b>/bitnami/moodle/local/wstemplate/docs_curated.php</b> on line <b>243</b><br />
string // 
				}
			]
		}
	}
]
userstats // 
{
	grade double // Attempt final grade.
	completed int // Time completed.
	timetotake int // Time taken.
	gradeinfo **Optional** // Attempt grade
	{
		nquestions int // Number of questions answered
		attempts int // Number of question attempts
		total double // Max points possible
		earned double // Points earned by student
		grade double // Calculated percentage grade
		nmanual int // Number of manually graded questions
		manualpoints double // Point value for manually graded questions
	}
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_user_attempt_grade</summary>
<br/>
<p>Return grade information in the attempt for a given user.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
lessonattempt int // lesson attempt number
userid int // the user id (empty for current user)
```

<h3>Returns</h3>
```
grade // Attempt grade
{
	nquestions int // Number of questions answered
	attempts int // Number of question attempts
	total double // Max points possible
	earned double // Points earned by student
	grade double // Calculated percentage grade
	nmanual int // Number of manually graded questions
	manualpoints double // Point value for manually graded questions
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_lesson_get_user_grade</summary>
<br/>
<p>Return the final grade in the lesson for the given user.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
userid int // the user id (empty for current user)
```

<h3>Returns</h3>
```
grade double // The lesson final raw grade
formattedgrade string // The lesson final grade formatted
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModPage</strong></td><td><details>
<summary>mod_page_get_pages_by_courses</summary>
<br/>
<p>Returns a list of pages in a provided list of courses, if no list is provided all pages that the user
                            can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
pages // 
[
	{
		id int // Module id
		coursemodule int // Course module id
		course int // Course id
		name string // Page name
		intro string // Summary
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		content string // Page content
		contentformat int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		contentfiles // Files in the content
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		legacyfiles int // Legacy files flag
		legacyfileslast int // Legacy files last control flag
		display int // How to display the page
		displayoptions string // Display options (width, height)
		revision int // Incremented when after each file changes, to avoid cache
		timemodified int // Last time the page was modified
		section int // Course section id
		visible int // Module visibility
		groupmode int // Group mode
		groupingid int // Grouping id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModQuiz</strong></td><td><details>
<summary>mod_quiz_get_attempt_access_information</summary>
<br/>
<p>Return access information for a given attempt in a quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
attemptid int // attempt id, 0 for the user last attempt if exists
```

<h3>Returns</h3>
```
endtime int **Optional** // When the attempt must be submitted (determined by rules).
isfinished int // Whether there is no way the user will ever be allowed to attempt.
ispreflightcheckrequired int **Optional** // whether a check is required before the user
                                                                    starts/continues his attempt.
preventnewattemptreasons // list of reasons
[
	{
		string // access restriction description
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_attempt_review</summary>
<br/>
<p>Returns review information for the given finished attempt, can be used by users or teachers.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
page int // page number, empty for all the questions in all the pages
```

<h3>Returns</h3>
```
grade string // grade for the quiz (or empty or "notyetgraded")
attempt // 
{
	id int **Optional** // Attempt id.
	quiz int **Optional** // Foreign key reference to the quiz that was attempted.
	userid int **Optional** // Foreign key reference to the user whose attempt this is.
	attempt int **Optional** // Sequentially numbers this students attempts at this quiz.
	uniqueid int **Optional** // Foreign key reference to the question_usage that holds the
                                                    details of the the question_attempts that make up this quiz
                                                    attempt.
	layout string **Optional** // Attempt layout.
	currentpage int **Optional** // Attempt current page.
	preview int **Optional** // Whether is a preview attempt or not.
	state string **Optional** // The current state of the attempts. 'inprogress',
                                                'overdue', 'finished' or 'abandoned'.
	timestart int **Optional** // Time when the attempt was started.
	timefinish int **Optional** // Time when the attempt was submitted.
                                                    0 if the attempt has not been submitted yet.
	timemodified int **Optional** // Last modified time.
	timemodifiedoffline int **Optional** // Last modified time via webservices.
	timecheckstate int **Optional** // Next time quiz cron should check attempt for
                                                        state changes.  NULL means never check.
	sumgrades double **Optional** // Total marks for this attempt.
}
additionaldata // 
[
	{
		id string // id of the data
		title string // data title
		content string // data content
	}
]
questions // 
[
	{
		slot int // slot number
		type string // question type, i.e: multichoice
		page int // page of the quiz this question appears on
		html string // the question rendered
		responsefileareas **Optional** // Response file areas including files
		[
			{
				area string // File area name
				files **Optional** // Response files for the question
				[
					{
						filename string **Optional** // File name.
						filepath string **Optional** // File path.
						filesize int **Optional** // File size.
						fileurl string **Optional** // Downloadable file url.
						timemodified int **Optional** // Time modified.
						mimetype string **Optional** // File mime type.
						isexternalfile int **Optional** // Whether is an external file.
						repositorytype string **Optional** // The repository type for external files.
					}
				]
			}
		]
		sequencecheck int **Optional** // the number of real steps in this attempt
		lastactiontime int **Optional** // the timestamp of the most recent step in this question attempt
		hasautosavedstep int **Optional** // whether this question attempt has autosaved data
		flagged int // whether the question is flagged or not
		number int **Optional** // question ordering number in the quiz
		state string **Optional** // the state where the question is in.
                    It will not be returned if the user cannot see it due to the quiz display correctness settings.
		status string **Optional** // current formatted state of the question
		blockedbyprevious int **Optional** // whether the question is blocked by the previous question
		mark string **Optional** // the mark awarded.
                    It will be returned only if the user is allowed to see it.
		maxmark double **Optional** // the maximum mark possible for this question attempt.
                    It will be returned only if the user is allowed to see it.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_combined_review_options</summary>
<br/>
<p>Combines the review options from a number of different quiz attempts.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
userid int // user id (empty for current user)
```

<h3>Returns</h3>
```
someoptions // 
[
	{
		name string // option name
		value int // option value
	}
]
alloptions // 
[
	{
		name string // option name
		value int // option value
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_quizzes_by_courses</summary>
<br/>
<p>Returns a list of quizzes in a provided list of courses,
                            if no list is provided all quizzes that the user can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
quizzes // 
[
	{
		id int // Standard Moodle primary key.
		course int // Foreign key reference to the course this quiz is part of.
		coursemodule int // Course module id.
		name string // Quiz name.
		intro string **Optional** // Quiz introduction text.
		introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timeopen int **Optional** // The time when this quiz opens. (0 = no restriction.)
		timeclose int **Optional** // The time when this quiz closes. (0 = no restriction.)
		timelimit int **Optional** // The time limit for quiz attempts, in seconds.
		overduehandling string **Optional** // The method used to handle overdue attempts.
                                                                    'autosubmit', 'graceperiod' or 'autoabandon'.
		graceperiod int **Optional** // The amount of time (in seconds) after the time limit
                                                                runs out during which attempts can still be submitted,
                                                                if overduehandling is set to allow it.
		preferredbehaviour string **Optional** // The behaviour to ask questions to use.
		canredoquestions int **Optional** // Allows students to redo any completed question
                                                                        within a quiz attempt.
		attempts int **Optional** // The maximum number of attempts a student is allowed.
		attemptonlast int **Optional** // Whether subsequent attempts start from the answer
                                                                    to the previous attempt (1) or start blank (0).
		grademethod int **Optional** // One of the values QUIZ_GRADEHIGHEST, QUIZ_GRADEAVERAGE,
                                                                    QUIZ_ATTEMPTFIRST or QUIZ_ATTEMPTLAST.
		decimalpoints int **Optional** // Number of decimal points to use when displaying
                                                                    grades.
		questiondecimalpoints int **Optional** // Number of decimal points to use when
                                                                            displaying question grades.
                                                                            (-1 means use decimalpoints.)
		reviewattempt int **Optional** // Whether users are allowed to review their quiz
                                                                    attempts at various times. This is a bit field, decoded by the
                                                                    mod_quiz_display_options class. It is formed by ORing together
                                                                    the constants defined there.
		reviewcorrectness int **Optional** // Whether users are allowed to review their quiz
                                                                        attempts at various times.
                                                                        A bit field, like reviewattempt.
		reviewmarks int **Optional** // Whether users are allowed to review their quiz attempts
                                                                at various times. A bit field, like reviewattempt.
		reviewspecificfeedback int **Optional** // Whether users are allowed to review their
                                                                            quiz attempts at various times. A bit field, like
                                                                            reviewattempt.
		reviewgeneralfeedback int **Optional** // Whether users are allowed to review their
                                                                            quiz attempts at various times. A bit field, like
                                                                            reviewattempt.
		reviewrightanswer int **Optional** // Whether users are allowed to review their quiz
                                                                        attempts at various times. A bit field, like
                                                                        reviewattempt.
		reviewoverallfeedback int **Optional** // Whether users are allowed to review their quiz
                                                                            attempts at various times. A bit field, like
                                                                            reviewattempt.
		questionsperpage int **Optional** // How often to insert a page break when editing
                                                                        the quiz, or when shuffling the question order.
		navmethod string **Optional** // Any constraints on how the user is allowed to navigate
                                                                around the quiz. Currently recognised values are
                                                                'free' and 'seq'.
		shuffleanswers int **Optional** // Whether the parts of the question should be shuffled,
                                                                    in those question types that support it.
		sumgrades double **Optional** // The total of all the question instance maxmarks.
		grade double **Optional** // The total that the quiz overall grade is scaled to be
                                                            out of.
		timecreated int **Optional** // The time when the quiz was added to the course.
		timemodified int **Optional** // Last modified time.
		password string **Optional** // A password that the student must enter before starting or
                                                                continuing a quiz attempt.
		subnet string **Optional** // Used to restrict the IP addresses from which this quiz can
                                                            be attempted. The format is as requried by the address_in_subnet
                                                            function.
		browsersecurity string **Optional** // Restriciton on the browser the student must
                                                                    use. E.g. 'securewindow'.
		delay1 int **Optional** // Delay that must be left between the first and second attempt,
                                                            in seconds.
		delay2 int **Optional** // Delay that must be left between the second and subsequent
                                                            attempt, in seconds.
		showuserpicture int **Optional** // Option to show the user's picture during the
                                                                    attempt and on the review page.
		showblocks int **Optional** // Whether blocks should be shown on the attempt.php and
                                                                review.php pages.
		completionattemptsexhausted int **Optional** // Mark quiz complete when the student has
                                                                                exhausted the maximum number of attempts
		completionpass int **Optional** // Whether to require passing grade
		allowofflineattempts int **Optional** // Whether to allow the quiz to be attempted
                                                                            offline in the mobile app
		autosaveperiod int **Optional** // Auto-save delay
		hasfeedback int **Optional** // Whether the quiz has any non-blank feedback text
		hasquestions int **Optional** // Whether the quiz has questions
		section int **Optional** // Course section id
		visible int **Optional** // Module visibility
		groupmode int **Optional** // Group mode
		groupingid int **Optional** // Grouping id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_quiz_access_information</summary>
<br/>
<p>Return access information for a given quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
```

<h3>Returns</h3>
```
canattempt int // Whether the user can do the quiz or not.
canmanage int // Whether the user can edit the quiz settings or not.
canpreview int // Whether the user can preview the quiz or not.
canreviewmyattempts int // Whether the users can review their previous attempts
                                                                or not.
canviewreports int // Whether the user can view the quiz reports or not.
accessrules // list of rules
[
	{
		string // rule description
	}
]
activerulenames // list of active rules
[
	{
		string // rule plugin names
	}
]
preventaccessreasons // list of reasons
[
	{
		string // access restriction description
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_quiz_required_qtypes</summary>
<br/>
<p>Return the potential question types that would be required for a given quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
```

<h3>Returns</h3>
```
questiontypes // list of question types used in the quiz
[
	{
		string // question type
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_user_attempts</summary>
<br/>
<p>Return a list of attempts for the given quiz and user.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
userid int // user id, empty for current user
status string // quiz status: all, finished or unfinished
includepreviews int // whether to include previews or not
```

<h3>Returns</h3>
```
attempts // 
[
	{
		id int **Optional** // Attempt id.
		quiz int **Optional** // Foreign key reference to the quiz that was attempted.
		userid int **Optional** // Foreign key reference to the user whose attempt this is.
		attempt int **Optional** // Sequentially numbers this students attempts at this quiz.
		uniqueid int **Optional** // Foreign key reference to the question_usage that holds the
                                                    details of the the question_attempts that make up this quiz
                                                    attempt.
		layout string **Optional** // Attempt layout.
		currentpage int **Optional** // Attempt current page.
		preview int **Optional** // Whether is a preview attempt or not.
		state string **Optional** // The current state of the attempts. 'inprogress',
                                                'overdue', 'finished' or 'abandoned'.
		timestart int **Optional** // Time when the attempt was started.
		timefinish int **Optional** // Time when the attempt was submitted.
                                                    0 if the attempt has not been submitted yet.
		timemodified int **Optional** // Last modified time.
		timemodifiedoffline int **Optional** // Last modified time via webservices.
		timecheckstate int **Optional** // Next time quiz cron should check attempt for
                                                        state changes.  NULL means never check.
		sumgrades double **Optional** // Total marks for this attempt.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_quiz_get_user_best_grade</summary>
<br/>
<p>Get the best current grade for the given user on a quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
userid int // user id
```

<h3>Returns</h3>
```
hasgrade int // Whether the user has a grade on the given quiz.
grade double **Optional** // The grade (only if the user has a grade).
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModResource</strong></td><td><details>
<summary>mod_resource_get_resources_by_courses</summary>
<br/>
<p>Returns a list of files in a provided list of courses, if no list is provided all files that
                            the user can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
resources // 
[
	{
		id int // Module id
		coursemodule int // Course module id
		course int // Course id
		name string // Page name
		intro string // Summary
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		contentfiles // Files in the content
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		tobemigrated int // Whether this resource was migrated
		legacyfiles int // Legacy files flag
		legacyfileslast int // Legacy files last control flag
		display int // How to display the resource
		displayoptions string // Display options (width, height)
		filterfiles int // If filters should be applied to the resource content
		revision int // Incremented when after each file changes, to avoid cache
		timemodified int // Last time the resource was modified
		section int // Course section id
		visible int // Module visibility
		groupmode int // Group mode
		groupingid int // Grouping id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModSurvey</strong></td><td><details>
<summary>mod_survey_get_questions</summary>
<br/>
<p>Get the complete list of questions for the survey, including subquestions.</p>
<h3>Parameters</h3>
```
surveyid int // survey instance id
```

<h3>Returns</h3>
```
questions // 
[
	{
		id int // Question id
		text string // Question text
		shorttext string // Question short text
		multi string // Subquestions ids
		intro string // The question intro
		type int // Question type
		options string // Question options
		parent int // Parent question (for subquestions)
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_survey_get_surveys_by_courses</summary>
<br/>
<p>Returns a list of survey instances in a provided set of courses,
                            if no courses are provided then all the survey instances the user has access to will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // course id
	}
]
```

<h3>Returns</h3>
```
surveys // 
[
	{
		id int // Survey id
		coursemodule int // Course module id
		course int // Course id
		name string // Survey name
		intro string **Optional** // The Survey intro
		introformat int **Optional** // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		template int **Optional** // Survey type
		days int **Optional** // Days
		questions string **Optional** // Question ids
		surveydone int **Optional** // Did I finish the survey?
		timecreated int **Optional** // Time of creation
		timemodified int **Optional** // Time of last modification
		section int **Optional** // Course section id
		visible int **Optional** // Visible
		groupmode int **Optional** // Group mode
		groupingid int **Optional** // Group id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModUrl</strong></td><td><details>
<summary>mod_url_get_urls_by_courses</summary>
<br/>
<p>Returns a list of urls in a provided list of courses, if no list is provided all urls that the user
                            can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
urls // 
[
	{
		id int // Module id
		coursemodule int // Course module id
		course int // Course id
		name string // URL name
		intro string // Summary
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		externalurl string // External URL
		display int // How to display the url
		displayoptions string // Display options (width, height)
		parameters string // Parameters to append to the URL
		timemodified int // Last time the url was modified
		section int // Course section id
		visible int // Module visibility
		groupmode int // Group mode
		groupingid int // Grouping id
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModWiki</strong></td><td><details>
<summary>mod_wiki_get_page_contents</summary>
<br/>
<p>Returns the contents of a page.</p>
<h3>Parameters</h3>
```
pageid int // Page ID.
```

<h3>Returns</h3>
```
page // Page
{
	id int // Page ID.
	wikiid int // Page's wiki ID.
	subwikiid int // Page's subwiki ID.
	groupid int // Page's group ID.
	userid int // Page's user ID.
	title string // Page title.
	cachedcontent string // Page contents.
	contentformat int **Optional** // cachedcontent format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	caneditpage int // True if user can edit the page.
	version int **Optional** // Latest version of the page.
	tags **Optional** // Tags
	[
		{
			id int // Tag id.
			name string // Tag name.
			rawname string // The raw, unnormalised name for the tag as entered by users.
			isstandard int // Whether this tag is standard.
			tagcollid int // Tag collection id.
			taginstanceid int // Tag instance id.
			taginstancecontextid int // Context the tag instance belongs to.
			itemid int // Id of the record tagged.
			ordering int // Tag ordering.
			flag int // Whether the tag is flagged as inappropriate.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_wiki_get_subwikis</summary>
<br/>
<p>Returns the list of subwikis the user can see in a specific wiki.</p>
<h3>Parameters</h3>
```
wikiid int // Wiki instance ID.
```

<h3>Returns</h3>
```
subwikis // 
[
	{
		id int // Subwiki ID.
		wikiid int // Wiki ID.
		groupid string // Group ID.
		userid int // User ID.
		canedit int // True if user can edit the subwiki.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_wiki_get_subwiki_files</summary>
<br/>
<p>Returns the list of files for a specific subwiki.</p>
<h3>Parameters</h3>
```
wikiid int // Wiki instance ID.
groupid int // Subwiki's group ID, -1 means current group. It will be ignored if the wiki doesn't use groups.
userid int // Subwiki's user ID, 0 means current user. It will be ignored in collaborative wikis.
```

<h3>Returns</h3>
```
files // Files
[
	{
		filename string **Optional** // File name.
		filepath string **Optional** // File path.
		filesize int **Optional** // File size.
		fileurl string **Optional** // Downloadable file url.
		timemodified int **Optional** // Time modified.
		mimetype string **Optional** // File mime type.
		isexternalfile int **Optional** // Whether is an external file.
		repositorytype string **Optional** // The repository type for external files.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_wiki_get_subwiki_pages</summary>
<br/>
<p>Returns the list of pages for a specific subwiki.</p>
<h3>Parameters</h3>
```
wikiid int // Wiki instance ID.
groupid int // Subwiki's group ID, -1 means current group. It will be ignored if the wiki doesn't use groups.
userid int // Subwiki's user ID, 0 means current user. It will be ignored in collaborative wikis.
options // Options
{
	sortby string // Field to sort by (id, title, ...).
	sortdirection string // Sort direction: ASC or DESC.
	includecontent int // Include each page contents or just the contents size.
}
```

<h3>Returns</h3>
```
pages // 
[
	{
		id int // Page ID.
		subwikiid int // Page's subwiki ID.
		title string // Page title.
		timecreated int // Time of creation.
		timemodified int // Time of last modification.
		timerendered int // Time of last renderization.
		userid int // ID of the user that last modified the page.
		pageviews int // Number of times the page has been viewed.
		readonly int // 1 if readonly, 0 otherwise.
		caneditpage int // True if user can edit the page.
		firstpage int // True if it's the first page.
		cachedcontent string **Optional** // Page contents.
		contentformat int **Optional** // cachedcontent format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		contentsize int **Optional** // Size of page contents in bytes (doesn't include size of attached files).
		tags **Optional** // Tags
		[
			{
				id int // Tag id.
				name string // Tag name.
				rawname string // The raw, unnormalised name for the tag as entered by users.
				isstandard int // Whether this tag is standard.
				tagcollid int // Tag collection id.
				taginstanceid int // Tag instance id.
				taginstancecontextid int // Context the tag instance belongs to.
				itemid int // Id of the record tagged.
				ordering int // Tag ordering.
				flag int // Whether the tag is flagged as inappropriate.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_wiki_get_wikis_by_courses</summary>
<br/>
<p>Returns a list of wiki instances in a provided set of courses, if no courses are provided then all the wiki instances the user has access to will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids.
[
	{
		int // Course ID
	}
]
```

<h3>Returns</h3>
```
wikis // 
[
	{
		id int // Wiki ID.
		coursemodule int // Course module ID.
		course int // Course ID.
		name string // Wiki name.
		intro string **Optional** // Wiki intro.
		introformat int **Optional** // Wiki intro format. format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		introfiles **Optional** // Files in the introduction text
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for external files.
			}
		]
		timecreated int **Optional** // Time of creation.
		timemodified int **Optional** // Time of last modification.
		firstpagetitle string **Optional** // First page title.
		wikimode string **Optional** // Wiki mode (individual, collaborative).
		defaultformat string **Optional** // Wiki's default format (html, creole, nwiki).
		forceformat int **Optional** // 1 if format is forced, 0 otherwise.
		editbegin int **Optional** // Edit begin.
		editend int **Optional** // Edit end.
		section int **Optional** // Course section ID.
		visible int **Optional** // 1 if visible, 0 otherwise.
		groupmode int **Optional** // Group mode.
		groupingid int **Optional** // Group ID.
		cancreatepages int // True if user can create pages.
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
</td></tr><tr><td><strong>ModWorkshop</strong></td><td><details>
<summary>mod_workshop_get_assessment</summary>
<br/>
<p>Retrieves the given assessment.</p>
<h3>Parameters</h3>
```
assessmentid int // Assessment id
```

<h3>Returns</h3>
```
assessment // 
{
	id int // The primary key of the record.
	submissionid int // The id of the assessed submission
	reviewerid int // The id of the reviewer who makes this assessment
	weight int // The weight of the assessment for the purposes of aggregation
	timecreated int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the first time
	timemodified int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the last time
	grade double // The aggregated grade for submission suggested by the reviewer.
                    The grade 0..100 is computed from the values assigned to the assessment dimensions fields. If NULL then it has not been aggregated yet.
	gradinggrade double // The computed grade 0..100 for this assessment. If NULL then it has not been computed yet.
	gradinggradeover double // Grade for the assessment manually overridden by a teacher.
                    Grade is always from interval 0..100. If NULL then the grade is not overriden.
	gradinggradeoverby int // The id of the user who has overridden the grade for submission.
	feedbackauthor string // The comment/feedback from the reviewer for the author.
	feedbackauthorformat int // feedbackauthor format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	feedbackauthorattachment int // Are there some files attached to the feedbackauthor field?
                    Sets to 1 by file_postupdate_standard_filemanager().
	feedbackreviewer string **Optional** // The comment/feedback from the teacher for the reviewer.
                    For example the reason why the grade for assessment was overridden
	feedbackreviewerformat int // feedbackreviewer format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	feedbackcontentfiles // feedbackcontentfiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
	feedbackattachmentfiles // feedbackattachmentfiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_grades</summary>
<br/>
<p>Returns the assessment and submission grade for the given user.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
userid int // User id (empty or 0 for current user).
```

<h3>Returns</h3>
```
assessmentrawgrade double **Optional** // The assessment raw (numeric) grade.
assessmentlongstrgrade string **Optional** // The assessment string grade.
assessmentgradehidden int **Optional** // Whether the grade is hidden or not.
submissionrawgrade double **Optional** // The submission raw (numeric) grade.
submissionlongstrgrade string **Optional** // The submission string grade.
submissiongradehidden int **Optional** // Whether the grade is hidden or not.
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_reviewer_assessments</summary>
<br/>
<p>Retrieves all the assessments reviewed by the given user.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
userid int // User id who did the assessment review (empty or 0 for current user).
```

<h3>Returns</h3>
```
assessments // 
[
	{
		id int // The primary key of the record.
		submissionid int // The id of the assessed submission
		reviewerid int // The id of the reviewer who makes this assessment
		weight int // The weight of the assessment for the purposes of aggregation
		timecreated int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the first time
		timemodified int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the last time
		grade double // The aggregated grade for submission suggested by the reviewer.
                    The grade 0..100 is computed from the values assigned to the assessment dimensions fields. If NULL then it has not been aggregated yet.
		gradinggrade double // The computed grade 0..100 for this assessment. If NULL then it has not been computed yet.
		gradinggradeover double // Grade for the assessment manually overridden by a teacher.
                    Grade is always from interval 0..100. If NULL then the grade is not overriden.
		gradinggradeoverby int // The id of the user who has overridden the grade for submission.
		feedbackauthor string // The comment/feedback from the reviewer for the author.
		feedbackauthorformat int // feedbackauthor format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		feedbackauthorattachment int // Are there some files attached to the feedbackauthor field?
                    Sets to 1 by file_postupdate_standard_filemanager().
		feedbackreviewer string **Optional** // The comment/feedback from the teacher for the reviewer.
                    For example the reason why the grade for assessment was overridden
		feedbackreviewerformat int // feedbackreviewer format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		feedbackcontentfiles // feedbackcontentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		feedbackattachmentfiles // feedbackattachmentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_submission</summary>
<br/>
<p>Retrieves the given submission.</p>
<h3>Parameters</h3>
```
submissionid int // Submission id
```

<h3>Returns</h3>
```
submission // 
{
	id int // The primary key of the record.
	workshopid int // The id of the workshop instance.
	example int // Is this submission an example from teacher.
	authorid int // The author of the submission.
	timecreated int // Timestamp when the work was submitted for the first time.
	timemodified int // Timestamp when the submission has been updated.
	title string // The submission title.
	content string // Submission text.
	contentformat int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	contenttrust int // The trust mode of the data.
	attachment int // Used by File API file_postupdate_standard_filemanager.
	grade double **Optional** // Aggregated grade for the submission. The grade is a decimal number from interval 0..100.
                    If NULL then the grade for submission has not been aggregated yet.
	gradeover double **Optional** // Grade for the submission manually overridden by a teacher. Grade is always from interval 0..100.
                    If NULL then the grade is not overriden.
	gradeoverby int **Optional** // The id of the user who has overridden the grade for submission.
	feedbackauthor string **Optional** // Teacher comment/feedback for the author of the submission, for example describing the reasons
                    for the grade overriding.
	feedbackauthorformat int // feedbackauthor format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	timegraded int **Optional** // The timestamp when grade or gradeover was recently modified.
	published int // Shall the submission be available to other when the workshop is closed.
	late int // Has this submission been submitted after the deadline or during the assessment phase?
	contentfiles **Optional** // contentfiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
	attachmentfiles **Optional** // attachmentfiles
	[
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
			isexternalfile int **Optional** // Whether is an external file.
			repositorytype string **Optional** // The repository type for the external files.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_submissions</summary>
<br/>
<p>Retrieves all the workshop submissions or the one done by the given user (except example submissions).</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
userid int // Get submissions done by this user. Use 0 or empty for the current user
groupid int // Group id, 0 means that the function will determine the user group.
                                                   It will return submissions done by users in the given group.
page int // The page of records to return.
perpage int // The number of records to return per page.
```

<h3>Returns</h3>
```
submissions // 
[
	{
		id int // The primary key of the record.
		workshopid int // The id of the workshop instance.
		example int // Is this submission an example from teacher.
		authorid int // The author of the submission.
		timecreated int // Timestamp when the work was submitted for the first time.
		timemodified int // Timestamp when the submission has been updated.
		title string // The submission title.
		content string // Submission text.
		contentformat int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		contenttrust int // The trust mode of the data.
		attachment int // Used by File API file_postupdate_standard_filemanager.
		grade double **Optional** // Aggregated grade for the submission. The grade is a decimal number from interval 0..100.
                    If NULL then the grade for submission has not been aggregated yet.
		gradeover double **Optional** // Grade for the submission manually overridden by a teacher. Grade is always from interval 0..100.
                    If NULL then the grade is not overriden.
		gradeoverby int **Optional** // The id of the user who has overridden the grade for submission.
		feedbackauthor string **Optional** // Teacher comment/feedback for the author of the submission, for example describing the reasons
                    for the grade overriding.
		feedbackauthorformat int // feedbackauthor format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		timegraded int **Optional** // The timestamp when grade or gradeover was recently modified.
		published int // Shall the submission be available to other when the workshop is closed.
		late int // Has this submission been submitted after the deadline or during the assessment phase?
		contentfiles **Optional** // contentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		attachmentfiles **Optional** // attachmentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
totalcount int // Total count of submissions.
totalfilesize int // Total size (bytes) of the files attached to all the
                    submissions (even the ones not returned due to pagination).
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_submission_assessments</summary>
<br/>
<p>Retrieves all the assessments of the given submission.</p>
<h3>Parameters</h3>
```
submissionid int // Submission id
```

<h3>Returns</h3>
```
assessments // 
[
	{
		id int // The primary key of the record.
		submissionid int // The id of the assessed submission
		reviewerid int // The id of the reviewer who makes this assessment
		weight int // The weight of the assessment for the purposes of aggregation
		timecreated int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the first time
		timemodified int // If 0 then the assessment was allocated but the reviewer has not assessed yet.
                    If greater than 0 then the timestamp of when the reviewer assessed for the last time
		grade double // The aggregated grade for submission suggested by the reviewer.
                    The grade 0..100 is computed from the values assigned to the assessment dimensions fields. If NULL then it has not been aggregated yet.
		gradinggrade double // The computed grade 0..100 for this assessment. If NULL then it has not been computed yet.
		gradinggradeover double // Grade for the assessment manually overridden by a teacher.
                    Grade is always from interval 0..100. If NULL then the grade is not overriden.
		gradinggradeoverby int // The id of the user who has overridden the grade for submission.
		feedbackauthor string // The comment/feedback from the reviewer for the author.
		feedbackauthorformat int // feedbackauthor format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		feedbackauthorattachment int // Are there some files attached to the feedbackauthor field?
                    Sets to 1 by file_postupdate_standard_filemanager().
		feedbackreviewer string **Optional** // The comment/feedback from the teacher for the reviewer.
                    For example the reason why the grade for assessment was overridden
		feedbackreviewerformat int // feedbackreviewer format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		feedbackcontentfiles // feedbackcontentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		feedbackattachmentfiles // feedbackattachmentfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_user_plan</summary>
<br/>
<p>Return the planner information for the given user.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
userid int // User id (empty or 0 for current user).
```

<h3>Returns</h3>
```
userplan // 
{
	phases // 
	[
		{
			code int // Phase code.
			title string // Phase title.
			active int // Whether is the active task.
			tasks // 
			[
				{
					code string // Task code.
					title string // Task title.
					link string // Link to task.
					details string **Optional** // Task details.
					completed string // Completion information (maybe empty, maybe a boolean or generic info.
				}
			]
			actions // 
			[
				{
					type string **Optional** // Action type.
					label string **Optional** // Action label.
					url string // Link to action.
					method string **Optional** // Get or post.
				}
			]
		}
	]
	examples // 
	[
		{
			id int // Example submission id.
			title string // Example submission title.
			assessmentid int // Example submission assessment id.
			grade double // The submission grade.
			gradinggrade double // The assessment grade.
		}
	]
}
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_workshops_by_courses</summary>
<br/>
<p>Returns a list of workshops in a provided list of courses, if no list is provided all workshops that
                            the user can view will be returned.</p>
<h3>Parameters</h3>
```
courseids // Array of course ids
[
	{
		int // Course id
	}
]
```

<h3>Returns</h3>
```
workshops // 
[
	{
		id int // The primary key of the record.
		course int // Course id this workshop is part of.
		name string // Workshop name.
		intro string // Workshop introduction text.
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		instructauthors string **Optional** // Instructions for the submission phase.
		instructauthorsformat int // instructauthors format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		instructreviewers string **Optional** // Instructions for the assessment phase.
		instructreviewersformat int // instructreviewers format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		timemodified int **Optional** // The timestamp when the module was modified.
		phase int **Optional** // The current phase of workshop (0 = not available, 1 = submission, 2 = assessment, 3 = closed).
		useexamples int **Optional** // Optional feature: students practise evaluating on example submissions from teacher.
		usepeerassessment int **Optional** // Optional feature: students perform peer assessment of others' work.
		useselfassessment int **Optional** // Optional feature: students perform self assessment of their own work.
		grade double **Optional** // The maximum grade for submission.
		gradinggrade double **Optional** // The maximum grade for assessment.
		strategy string **Optional** // The type of the current grading strategy used in this workshop.
		evaluation string **Optional** // The recently used grading evaluation method.
		gradedecimals int **Optional** // Number of digits that should be shown after the decimal point when displaying grades.
		submissiontypetext int **Optional** // Indicates whether text is required as part of each submission. 0 for no, 1 for optional, 2 for required.
		submissiontypefile int **Optional** // Indicates whether a file upload is required as part of each submission. 0 for no, 1 for optional, 2 for required.
		nattachments int **Optional** // Maximum number of submission attachments.
		submissionfiletypes string **Optional** // Comma separated list of file extensions.
		latesubmissions int **Optional** // Allow submitting the work after the deadline.
		maxbytes int **Optional** // Maximum size of the one attached file.
		examplesmode int **Optional** // 0 = example assessments are voluntary, 1 = examples must be assessed before submission,
                    2 = examples are available after own submission and must be assessed before peer/self assessment phase.
		submissionstart int **Optional** // 0 = will be started manually, greater than 0 the timestamp of the start of the submission phase.
		submissionend int **Optional** // 0 = will be closed manually, greater than 0 the timestamp of the end of the submission phase.
		assessmentstart int **Optional** // 0 = will be started manually, greater than 0 the timestamp of the start of the assessment phase.
		assessmentend int **Optional** // 0 = will be closed manually, greater than 0 the timestamp of the end of the assessment phase.
		phaseswitchassessment int **Optional** // Automatically switch to the assessment phase after the submissions deadline.
		conclusion string **Optional** // A text to be displayed at the end of the workshop.
		conclusionformat int // conclusion format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		overallfeedbackmode int **Optional** // Mode of the overall feedback support.
		overallfeedbackfiles int **Optional** // Number of allowed attachments to the overall feedback.
		overallfeedbackfiletypes string **Optional** // Comma separated list of file extensions.
		overallfeedbackmaxbytes int **Optional** // Maximum size of one file attached to the overall feedback.
		coursemodule int // coursemodule
		introfiles // introfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		instructauthorsfiles **Optional** // instructauthorsfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		instructreviewersfiles **Optional** // instructreviewersfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
		conclusionfiles **Optional** // conclusionfiles
		[
			{
				filename string **Optional** // File name.
				filepath string **Optional** // File path.
				filesize int **Optional** // File size.
				fileurl string **Optional** // Downloadable file url.
				timemodified int **Optional** // Time modified.
				mimetype string **Optional** // File mime type.
				isexternalfile int **Optional** // Whether is an external file.
				repositorytype string **Optional** // The repository type for the external files.
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_workshop_get_workshop_access_information</summary>
<br/>
<p>Return access information for a given workshop.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
```

<h3>Returns</h3>
```
creatingsubmissionallowed int // Is the given user allowed to create their submission?
modifyingsubmissionallowed int // Is the user allowed to modify his existing submission?
assessingallowed int // Is the user allowed to create/edit his assessments?
assessingexamplesallowed int // Are reviewers allowed to create/edit their assessments of the example submissions?.
examplesassessedbeforesubmission int // Whether the given user has assessed all his required examples before submission
                (always true if there are not examples to assess or not configured to check before submission).
examplesassessedbeforeassessment int // Whether the given user has assessed all his required examples before assessment
                (always true if there are not examples to assessor not configured to check before assessment).
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item
		itemid int **Optional** // item id
		warningcode string // the warning code can be used by the client app to implement specific behaviour
		message string // untranslated english message to explain the warning
	}
]
canview int // Whether the user has the capability mod/workshop:view allowed.
canaddinstance int // Whether the user has the capability mod/workshop:addinstance allowed.
canswitchphase int // Whether the user has the capability mod/workshop:switchphase allowed.
caneditdimensions int // Whether the user has the capability mod/workshop:editdimensions allowed.
cansubmit int // Whether the user has the capability mod/workshop:submit allowed.
canpeerassess int // Whether the user has the capability mod/workshop:peerassess allowed.
canmanageexamples int // Whether the user has the capability mod/workshop:manageexamples allowed.
canallocate int // Whether the user has the capability mod/workshop:allocate allowed.
canpublishsubmissions int // Whether the user has the capability mod/workshop:publishsubmissions allowed.
canviewauthornames int // Whether the user has the capability mod/workshop:viewauthornames allowed.
canviewreviewernames int // Whether the user has the capability mod/workshop:viewreviewernames allowed.
canviewallsubmissions int // Whether the user has the capability mod/workshop:viewallsubmissions allowed.
canviewpublishedsubmissions int // Whether the user has the capability mod/workshop:viewpublishedsubmissions allowed.
canviewauthorpublished int // Whether the user has the capability mod/workshop:viewauthorpublished allowed.
canviewallassessments int // Whether the user has the capability mod/workshop:viewallassessments allowed.
canoverridegrades int // Whether the user has the capability mod/workshop:overridegrades allowed.
canignoredeadlines int // Whether the user has the capability mod/workshop:ignoredeadlines allowed.
candeletesubmissions int // Whether the user has the capability mod/workshop:deletesubmissions allowed.
canexportsubmissions int // Whether the user has the capability mod/workshop:exportsubmissions allowed.
```

<hr/>
</details>
</td></tr><tr><td><strong>block</strong></td><td><details>
<summary>block_recentlyaccesseditems_get_recent_items</summary>
<br/>
<p>List of items a user has accessed most recently.</p>
<h3>Parameters</h3>
```
limit int // result set limit
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>block_starredcourses_get_starred_courses</summary>
<br/>
<p>Get users starred courses.</p>
<h3>Parameters</h3>
```
limit int // Limit
offset int // Offset
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
</td></tr></tbody></table>