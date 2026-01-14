# Function Documentation

The following documentation is extracted from the auto-generated moodle API documentation. This list can be overwhelming, as there is much functionality that is either irrelevant to students or even inaccessible to students. Consider looking at [curated functions](functions.md) first, where we list functions that we consider to be potentially relevant for students.

<details>
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
<details>
<summary>core_badges_get_user_badges</summary>
<br/>
<p>Returns the list of badges awarded to a user.</p>
<h3>Parameters</h3>
```
userid int // Badges only for this user id, empty for current user
courseid int // Filter badges by course id, empty all the courses
page int // The page of records to return.
perpage int // The number of records to return per page
search string // A simple string to search for
onlypublic int // Whether to return only public badges
```

<h3>Returns</h3>
```
badges // 
[
	{
		id int **Optional** // Badge id
		name string // Badge name
		description string // Badge description
		timecreated int **Optional** // Time created
		timemodified int **Optional** // Time modified
		usercreated int **Optional** // User created
		usermodified int **Optional** // User modified
		issuername string // Issuer name
		issuerurl string // Issuer URL
		issuercontact string // Issuer contact
		expiredate int **Optional** // Expire date
		expireperiod int **Optional** // Expire period
		type int **Optional** // Type
		courseid int **Optional** // Course id
		message string **Optional** // Message
		messagesubject string **Optional** // Message subject
		attachment int **Optional** // Attachment
		notification int **Optional** // Whether to notify when badge is awarded
		nextcron int **Optional** // Next cron
		status int **Optional** // Status
		issuedid int **Optional** // Issued id
		uniquehash string // Unique hash
		dateissued int // Date issued
		dateexpire int // Date expire
		visible int **Optional** // Visible
		email string **Optional** // User email
		version string **Optional** // Version
		language string **Optional** // Language
		imageauthorname string **Optional** // Name of the image author
		imageauthoremail string **Optional** // Email of the image author
		imageauthorurl string **Optional** // URL of the image author
		imagecaption string **Optional** // Caption of the image
		badgeurl string // Badge URL
		endorsement **Optional** // 
		{
			id int // Endorsement id
			badgeid int // Badge id
			issuername string // Endorsement issuer name
			issuerurl string // Endorsement issuer URL
			issueremail string // Endorsement issuer email
			claimid string // Claim URL
			claimcomment string // Claim comment
			dateissued int // Date issued
		}
		alignment // Badge alignments
		[
			{
				id int **Optional** // Alignment id
				badgeid int **Optional** // Badge id
				targetName string **Optional** // Target name
				targetUrl string **Optional** // Target URL
				targetDescription string **Optional** // Target description
				targetFramework string **Optional** // Target framework
				targetCode string **Optional** // Target code
			}
		]
		relatedbadges // Related badges
		[
			{
				id int // Badge id
				name string // Badge name
				version string **Optional** // Version
				language string **Optional** // Language
				type int **Optional** // Type
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
<summary>core_block_get_course_blocks</summary>
<br/>
<p>Returns blocks information for a course.</p>
<h3>Parameters</h3>
```
courseid int // course id
returncontents int // Whether to return the block contents.
```

<h3>Returns</h3>
```
blocks // List of blocks in the course.
[
	{
		instanceid int // Block instance id.
		name string // Block name.
		region string // Block region.
		positionid int // Position id.
		collapsible int // Whether the block is collapsible.
		dockable int // Whether the block is dockable.
		weight int **Optional** // Used to order blocks within a region.
		visible int **Optional** // Whether the block is visible.
		contents **Optional** // Block contents (if required).
		{
			title string // Block title.
			content string // Block contents.
			contentformat int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			footer string // Block footer.
			files // Block files.
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
		configs **Optional** // Block instance and plugin configuration settings.
		[
			{
				name string // Name.
				value string // JSON encoded representation of the config value.
				type string // Type (instance or plugin).
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
<summary>core_block_get_dashboard_blocks</summary>
<br/>
<p>Returns blocks information for the given user dashboard.</p>
<h3>Parameters</h3>
```
userid int // User id (optional), default is current user.
returncontents int // Whether to return the block contents.
```

<h3>Returns</h3>
```
blocks // List of blocks in the dashboard.
[
	{
		instanceid int // Block instance id.
		name string // Block name.
		region string // Block region.
		positionid int // Position id.
		collapsible int // Whether the block is collapsible.
		dockable int // Whether the block is dockable.
		weight int **Optional** // Used to order blocks within a region.
		visible int **Optional** // Whether the block is visible.
		contents **Optional** // Block contents (if required).
		{
			title string // Block title.
			content string // Block contents.
			contentformat int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			footer string // Block footer.
			files // Block files.
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
		configs **Optional** // Block instance and plugin configuration settings.
		[
			{
				name string // Name.
				value string // JSON encoded representation of the config value.
				type string // Type (instance or plugin).
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
<summary>core_blog_get_entries</summary>
<br/>
<p>Returns blog entries.</p>
<h3>Parameters</h3>
```
filters // Parameters to filter blog listings.
[
	{
		name string // The expected keys (value format) are:
                                tag      PARAM_NOTAGS blog tag
                                tagid    PARAM_INT    blog tag id
                                userid   PARAM_INT    blog author (userid)
                                cmid    PARAM_INT    course module id
                                entryid  PARAM_INT    entry id
                                groupid  PARAM_INT    group id
                                courseid PARAM_INT    course id
                                search   PARAM_RAW    search term
                                
		value string // The value of the filter.
	}
]
page int // The blog page to return.
perpage int // The number of posts to return per page.
```

<h3>Returns</h3>
```
entries // 
[
	{
		id int // Post/entry id.
		module string // Where it was published the post (blog, blog_external...).
		userid int // Post author.
		courseid int // Course where the post was created.
		groupid int // Group post was created for.
		moduleid int // Module id where the post was created (not used anymore).
		coursemoduleid int // Course module id where the post was created.
		subject string // Post subject.
		summary string // Post summary.
		summaryformat int // summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		content string // Post content.
		uniquehash string // Post unique hash.
		rating int // Post rating.
		format int // Post content format.
		attachment string // Post atachment.
		publishstate string // Post publish state.
		lastmodified int // When it was last modified.
		created int // When it was created.
		usermodified int // User that updated the post.
		summaryfiles // summaryfiles
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
totalentries int // The total number of entries found.
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
<summary>core_blog_view_entries</summary>
<br/>
<p>Trigger the blog_entries_viewed event.</p>
<h3>Parameters</h3>
```
filters // Parameters used in the filter of view_entries.
[
	{
		name string // The expected keys (value format) are:
                                tag      PARAM_NOTAGS blog tag
                                tagid    PARAM_INT    blog tag id
                                userid   PARAM_INT    blog author (userid)
                                cmid     PARAM_INT    course module id
                                entryid  PARAM_INT    entry id
                                groupid  PARAM_INT    group id
                                courseid PARAM_INT    course id
                                search   PARAM_RAW    search term
                                
		value string // The value of the filter.
	}
]
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_calendar_get_allowed_event_types</summary>
<br/>
<p>Get the type of events a user can create in the given course.</p>
<h3>Parameters</h3>
```
courseid int // Course to check, empty for site.
```

<h3>Returns</h3>
```
allowedeventtypes // 
[
	{
		string // Allowed event types to be created in the given course.
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
<summary>core_calendar_get_calendar_access_information</summary>
<br/>
<p>Convenience function to retrieve some permissions/access information for the given course calendar.</p>
<h3>Parameters</h3>
```
courseid int // Course to check, empty for site calendar events.
```

<h3>Returns</h3>
```
canmanageentries int // Whether the user can manage entries.
canmanageownentries int // Whether the user can manage its own entries.
canmanagegroupentries int // Whether the user can manage group entries.
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
<summary>core_calendar_get_calendar_export_token</summary>
<br/>
<p>Return the auth token required for exporting a calendar.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
token string // The calendar permanent access token for calendar export.
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
<summary>core_calendar_get_calendar_monthly_view</summary>
<br/>
<p>Fetch the monthly view data for a calendar</p>
<h3>Parameters</h3>
```
year int // Year to be viewed
month int // Month to be viewed
courseid int // Course being viewed
categoryid int // Category being viewed
includenavigation int // Whether to show course navigation
mini int // Whether to return the mini month view or not
day int // Day to be viewed
```

<h3>Returns</h3>
```
url string // url
courseid int // courseid
categoryid int **Optional** // categoryid
filter_selector string **Optional** // filter_selector
weeks // weeks
[
	{
		prepadding // prepadding
		[
			{
		int // prepadding
			}
		]
		postpadding // postpadding
		[
			{
		int // postpadding
			}
		]
		days // days
		[
			{
				seconds int // seconds
				minutes int // minutes
				hours int // hours
				mday int // mday
				wday int // wday
				year int // year
				yday int // yday
				istoday int // istoday
				isweekend int // isweekend
				timestamp int // timestamp
				neweventtimestamp int // neweventtimestamp
				viewdaylink string **Optional** // viewdaylink
				viewdaylinktitle string **Optional** // viewdaylinktitle
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
				hasevents int // hasevents
				calendareventtypes // calendareventtypes
				[
					{
		string // calendareventtypes
					}
				]
				previousperiod int // previousperiod
				nextperiod int // nextperiod
				navigation string // navigation
				haslastdayofevent int // haslastdayofevent
				popovertitle string // popovertitle
				daytitle string // daytitle
			}
		]
	}
]
daynames // daynames
[
	{
		dayno int // dayno
		shortname string // shortname
		fullname string // fullname
	}
]
view string // view
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
includenavigation int // includenavigation
initialeventsloaded int // initialeventsloaded
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
defaulteventcontext int // defaulteventcontext
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
<summary>core_calendar_submit_create_update_form</summary>
<br/>
<p>Submit form data for event form</p>
<h3>Parameters</h3>
```
formdata string // The data from the event form
```

<h3>Returns</h3>
```
event **Optional** // 
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
validationerror int // Invalid form data
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
<details>
<summary>core_comment_add_comments</summary>
<br/>
<p>Adds a comment or comments.</p>
<h3>Parameters</h3>
```
comments // 
[
	{
		contextlevel string // contextlevel system, course, user...
		instanceid int // the id of item associated with the contextlevel
		component string // component
		content string // component
		itemid int // associated id
		area string // string comment area
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_comment_delete_comments</summary>
<br/>
<p>Deletes a comment or comments.</p>
<h3>Parameters</h3>
```
comments // 
[
	{
		int // id of the comment
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_comment_get_comments</summary>
<br/>
<p>Returns comments.</p>
<h3>Parameters</h3>
```
contextlevel string // contextlevel system, course, user...
instanceid int // the Instance id of item associated with the context level
component string // component
itemid int // associated id
area string // string comment area
page int // page number (0 based)
sortdirection string // Sort direction: ASC or DESC
```

<h3>Returns</h3>
```
comments // List of comments
[
	{
		id int // Comment ID
		content string // The content text formatted
		format int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		timecreated int // Time created (timestamp)
		strftimeformat string // Time format
		profileurl string // URL profile
		fullname string // fullname
		time string // Time in human format
		avatar string // HTML user picture
		userid int // User ID
		delete int **Optional** // Permission to delete=true/false
	}
]
count int **Optional** // Total number of comments.
perpage int **Optional** // Number of comments per page.
canpost int **Optional** // Whether the user can post in this comment area.
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
<summary>core_competency_competency_viewed</summary>
<br/>
<p>Log event competency viewed</p>
<h3>Parameters</h3>
```
id int // The competency id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_delete_evidence</summary>
<br/>
<p>Delete an evidence</p>
<h3>Parameters</h3>
```
id int // The evidence ID
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_get_scale_values</summary>
<br/>
<p>Fetch the values for a specific scale</p>
<h3>Parameters</h3>
```
scaleid int // The scale id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_grade_competency_in_course</summary>
<br/>
<p>Grade a competency from the course page.</p>
<h3>Parameters</h3>
```
courseid int // Course id
userid int // User id
competencyid int // Competency id
grade int // New grade
note string // A note to attach to the evidence
```

<h3>Returns</h3>
```
usercompetencyid int // usercompetencyid
contextid int // contextid
action int // action
actionuserid int // actionuserid
descidentifier string // descidentifier
desccomponent string // desccomponent
desca string // desca
url string // url
grade int // grade
note string // note
id int // id
timecreated int // timecreated
timemodified int // timemodified
usermodified int // usermodified
actionuser **Optional** // 
{
	id int // id
	email string // email
	idnumber string // idnumber
	phone1 string // phone1
	phone2 string // phone2
	department string // department
	institution string // institution
	fullname string // fullname
	identity string // identity
	profileurl string // profileurl
	profileimageurl string // profileimageurl
	profileimageurlsmall string // profileimageurlsmall
}
description string // description
gradename string // gradename
userdate string // userdate
candelete int // candelete
```

<hr/>
</details>
<details>
<summary>core_competency_list_course_competencies</summary>
<br/>
<p>List the competencies in a course</p>
<h3>Parameters</h3>
```
id int // The course id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_user_competency_plan_viewed</summary>
<br/>
<p>Log the user competency plan viewed event.</p>
<h3>Parameters</h3>
```
competencyid int // The competency id
userid int // The user id
planid int // The plan id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_user_competency_viewed</summary>
<br/>
<p>Log the user competency viewed event.</p>
<h3>Parameters</h3>
```
usercompetencyid int // The user competency id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_user_competency_viewed_in_course</summary>
<br/>
<p>Log the user competency viewed in course event</p>
<h3>Parameters</h3>
```
competencyid int // The competency id
userid int // The user id
courseid int // The course id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_competency_user_competency_viewed_in_plan</summary>
<br/>
<p>Log the user competency viewed in plan event.</p>
<h3>Parameters</h3>
```
competencyid int // The competency id
userid int // The user id
planid int // The plan id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_completion_get_activities_completion_status</summary>
<br/>
<p>Return the activities completion status for a user in a course.</p>
<h3>Parameters</h3>
```
courseid int // Course ID
userid int // User ID
```

<h3>Returns</h3>
```
statuses // List of activities status
[
	{
		cmid int // comment ID
		modname string // activity module name
		instance int // instance ID
		state int // completion state value:
                                                                    0 means incomplete, 1 complete,
                                                                    2 complete pass, 3 complete fail
		timecompleted int // timestamp for completed activity
		tracking int // type of tracking:
                                                                    0 means none, 1 manual, 2 automatic
		overrideby int **Optional** // The user id who has overriden the status, or null
		valueused int **Optional** // Whether the completion status affects the availability
                                    of another activity.
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
<summary>core_completion_get_course_completion_status</summary>
<br/>
<p>Returns course completion status.</p>
<h3>Parameters</h3>
```
courseid int // Course ID
userid int // User ID
```

<h3>Returns</h3>
```
completionstatus // Course status
{
	completed int // true if the course is complete, false otherwise
	aggregation int // aggregation method 1 means all, 2 means any
	completions // 
	[
		{
			type int // Completion criteria type
			title string // Completion criteria Title
			status string // Completion status (Yes/No) a % or number
			complete int // Completion status (true/false)
			timecompleted int // Timestamp for criteria completetion
			details // details
			{
				type string // Type description
				criteria string // Criteria description
				requirement string // Requirement description
				status string // Status description, can be anything
			}
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
<summary>core_completion_mark_course_self_completed</summary>
<br/>
<p>Update the course completion status for the current user (if course self-completion is enabled).</p>
<h3>Parameters</h3>
```
courseid int // Course ID
```

<h3>Returns</h3>
```
status int // status, true if success
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
<summary>core_completion_update_activity_completion_status_manually</summary>
<br/>
<p>Update completion status for the current user in an activity, only for activities with manual tracking.</p>
<h3>Parameters</h3>
```
cmid int // course module id
completed int // activity completed or not
```

<h3>Returns</h3>
```
status int // status, true if success
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
<summary>core_course_check_updates</summary>
<br/>
<p>Check if there is updates affecting the user for the given course and contexts.</p>
<h3>Parameters</h3>
```
courseid int // Course id to check
tocheck // Instances to check
[
	{
		contextlevel string // The context level for the file location.
                                                                                Only module supported right now.
		id int // Context instance id
		since int // Check updates since this time stamp
	}
]
filter // Check only for updates in these areas
[
	{
		string // Area name: configuration, fileareas, completion, ratings, comments,
                                                        gradeitems, outcomes
	}
]
```

<h3>Returns</h3>
```
instances // 
[
	{
		contextlevel string // The context level
		id int // Instance id
		updates // 
		[
			{
				name string // Name of the area updated.
				timeupdated int **Optional** // Last time was updated
				itemids **Optional** // The ids of the items updated
				[
					{
		int // Instance id
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
<summary>core_course_get_categories</summary>
<br/>
<p>Return category details</p>
<h3>Parameters</h3>
```
criteria // criteria
[
	{
		key string // The category column to search, expected keys (value format) are:"id" (int) the category id,"ids" (string) category ids separated by commas,"name" (string) the category name,"parent" (int) the parent category id,"idnumber" (string) category idnumber - user must have 'moodle/category:manage' to search on idnumber,"visible" (int) whether the returned categories must be visible or hidden. If the key is not passed,
                                             then the function return all categories that the user can see. - user must have 'moodle/category:manage' or 'moodle/category:viewhiddencategories' to search on visible,"theme" (string) only return the categories having this theme - user must have 'moodle/category:manage' to search on theme
		value string // the value to match
	}
]
addsubcategories int // return the sub categories infos
                                          (1 - default) otherwise only the category info (0)
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
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
<summary>core_course_get_courses</summary>
<br/>
<p>Return course details</p>
<h3>Parameters</h3>
```
options // options - operator OR is used
{
	ids **Optional** // List of course id. If empty return all courses
                                            except front page course.
	[
		{
		int // Course id
		}
	]
}
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
<summary>core_course_get_course_module_by_instance</summary>
<br/>
<p>Return information about a given module name and instance id</p>
<h3>Parameters</h3>
```
module string // The module name
instance int // The module instance id
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
<summary>core_course_get_recent_courses</summary>
<br/>
<p>List of courses a user has accessed most recently.</p>
<h3>Parameters</h3>
```
userid int // id of the user, default to current user
limit int // result set limit
offset int // Result set offset
sort string // Sort string
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_course_get_updates_since</summary>
<br/>
<p>Check if there are updates affecting the user for the given course since the given time stamp.</p>
<h3>Parameters</h3>
```
courseid int // Course id to check
since int // Check updates since this time stamp
filter // Check only for updates in these areas
[
	{
		string // Area name: configuration, fileareas, completion, ratings, comments,
                                                        gradeitems, outcomes
	}
]
```

<h3>Returns</h3>
```
instances // 
[
	{
		contextlevel string // The context level
		id int // Instance id
		updates // 
		[
			{
				name string // Name of the area updated.
				timeupdated int **Optional** // Last time was updated
				itemids **Optional** // The ids of the items updated
				[
					{
		int // Instance id
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
<summary>core_course_get_user_administration_options</summary>
<br/>
<p>Return a list of administration options in a set of courses that are avaialable or not for the current
                            user.</p>
<h3>Parameters</h3>
```
courseids // 
[
	{
		int // Course id.
	}
]
```

<h3>Returns</h3>
```
courses // List of courses
[
	{
		id int // Course id
		options // 
		[
			{
				name string // Option name
				available int // Whether the option is available or not
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
<summary>core_course_get_user_navigation_options</summary>
<br/>
<p>Return a list of navigation options in a set of courses that are avaialable or not for the current user.</p>
<h3>Parameters</h3>
```
courseids // 
[
	{
		int // Course id.
	}
]
```

<h3>Returns</h3>
```
courses // List of courses
[
	{
		id int // Course id
		options // 
		[
			{
				name string // Option name
				available int // Whether the option is available or not
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
<details>
<summary>core_course_view_course</summary>
<br/>
<p>Log that the course was viewed</p>
<h3>Parameters</h3>
```
courseid int // id of the course
sectionnumber int // section number
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_enrol_get_course_enrolment_methods</summary>
<br/>
<p>Get the list of course enrolment methods</p>
<h3>Parameters</h3>
```
courseid int // Course id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_enrol_get_enrolled_users</summary>
<br/>
<p>Get enrolled users by course id.</p>
<h3>Parameters</h3>
```
courseid int // course id
options // Option names:
                            * withcapability (string) return only users with this capability. This option requires 'moodle/role:review' on the course context.
                            * groupid (integer) return only users in this group id. If the course has groups enabled and this param
                                                isn't defined, returns all the viewable users.
                                                This option requires 'moodle/site:accessallgroups' on the course context if the
                                                user doesn't belong to the group.
                            * onlyactive (integer) return only users with active enrolments and matching time restrictions. This option requires 'moodle/course:enrolreview' on the course context.
                            * userfields ('string, string, ...') return only the values of these user fields.
                            * limitfrom (integer) sql limit from.
                            * limitnumber (integer) maximum number of returned users.
                            * sortby (string) sort by id, firstname or lastname. For ordering like the site does, use siteorder.
                            * sortdirection (string) ASC or DESC
[
	{
		name string // option name
		value string // option value
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_enrol_get_users_courses</summary>
<br/>
<p>Get the list of courses where a user is enrolled in</p>
<h3>Parameters</h3>
```
userid int // user id
returnusercount int // Include count of enrolled users for each course? This can add several seconds to the response time if a user is on several large courses, so set this to false if the value will not be used to improve performance.
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_enrol_search_users</summary>
<br/>
<p>Search within the list of course participants</p>
<h3>Parameters</h3>
```
courseid int // course id
search string // query
searchanywhere int // find a match anywhere, or only at the beginning
page int // Page number
perpage int // Number per page
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_files_delete_draft_files</summary>
<br/>
<p>Delete the indicated files (or directories) from a user draft file area.</p>
<h3>Parameters</h3>
```
draftitemid int // Item id of the draft file area
files // Files or directories to be deleted.
[
	{
		filepath string // Path to the file or directory to delete.
		filename string // Name of the file to delete.
	}
]
```

<h3>Returns</h3>
```
parentpaths // 
[
	{
		string // Path to parent directory of the deleted files.
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
<summary>core_files_get_files</summary>
<br/>
<p>browse moodle files</p>
<h3>Parameters</h3>
```
contextid int // context id Set to -1 to use contextlevel and instanceid.
component string // component
filearea string // file area
itemid int // associated id
filepath string // file path
filename string // file name
modified int // timestamp to return files changed after this time.
contextlevel string // The context level for the file location.
instanceid int // The instance id for where the file is located.
```

<h3>Returns</h3>
```
parents // 
[
	{
		contextid int // 
		component string // 
		filearea string // 
		itemid int // 
		filepath string // 
		filename string // 
	}
]
files // 
[
	{
		contextid int // 
		component string // 
		filearea string // 
		itemid int // 
		filepath string // 
		filename string // 
		isdir int // 
		url string // 
		timemodified int // 
		timecreated int **Optional** // Time created
		filesize int **Optional** // File size
		author string **Optional** // File owner
		license string **Optional** // File license
	}
]
```

<hr/>
</details>
<details>
<summary>core_filters_get_available_in_context</summary>
<br/>
<p>Returns the filters available in the given contexts.</p>
<h3>Parameters</h3>
```
contexts // The list of contexts to check.
[
	{
		contextlevel string // The context level where the filters are:
                                (coursecat, course, module)
		instanceid int // The instance id of item associated with the context.
	}
]
```

<h3>Returns</h3>
```
filters // Available filters
[
	{
		contextlevel string // The context level where the filters are:
                                (coursecat, course, module).
		instanceid int // The instance id of item associated with the context.
		contextid int // The context id.
		filter string // Filter plugin name.
		localstate int // Filter state: 1 for on, -1 for off, 0 if inherit.
		inheritedstate int // 1 or 0 to use when localstate is set to inherit.
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
<summary>core_get_component_strings</summary>
<br/>
<p>Return all raw strings (with {$a->xxx}), for a specific component - similar to core get_component_strings(), call</p>
<h3>Parameters</h3>
```
component string // component
lang string // lang
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_grades_grader_gradingpanel_point_fetch</summary>
<br/>
<p>Fetch the data required to display the grader grading panel for simple grading, creating the grade item if required</p>
<h3>Parameters</h3>
```
component string // The name of the component
contextid int // The ID of the context being graded
itemname string // The grade item itemname being graded
gradeduserid int // The ID of the user show
```

<h3>Returns</h3>
```
templatename string // The template to use when rendering this data
hasgrade int // Does the user have a grade?
grade // 
{
	grade double // The numeric grade
	usergrade string // Current user grade
	maxgrade string // Max possible grade
	gradedby string // The assumed grader of this grading instance
	timecreated int // The time that the grade was created
	timemodified int // The time that the grade was last updated
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
<summary>core_grades_grader_gradingpanel_point_store</summary>
<br/>
<p>Store the data required to display the grader grading panel for simple grading</p>
<h3>Parameters</h3>
```
component string // The name of the component
contextid int // The ID of the context being graded
itemname string // The grade item itemname being graded
gradeduserid int // The ID of the user show
notifyuser int // Wheteher to notify the user or not
formdata string // The serialised form data representing the grade
```

<h3>Returns</h3>
```
templatename string // The template to use when rendering this data
hasgrade int // Does the user have a grade?
grade // 
{
	grade double // The numeric grade
	usergrade string // Current user grade
	maxgrade string // Max possible grade
	gradedby string // The assumed grader of this grading instance
	timecreated int // The time that the grade was created
	timemodified int // The time that the grade was last updated
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
<summary>core_grades_grader_gradingpanel_scale_fetch</summary>
<br/>
<p>Fetch the data required to display the grader grading panel for scale-based grading, creating the grade item if required</p>
<h3>Parameters</h3>
```
component string // The name of the component
contextid int // The ID of the context being graded
itemname string // The grade item itemname being graded
gradeduserid int // The ID of the user show
```

<h3>Returns</h3>
```
templatename string // The template to use when rendering this data
hasgrade int // Does the user have a grade?
grade // 
{
	options // The description of the grade option
	[
		{
			value double // The grade value
			title string // The description fo the option
			selected int // Whether this item is currently selected
		}
	]
	usergrade string // Current user grade
	maxgrade string // Max possible grade
	gradedby string // The assumed grader of this grading instance
	timecreated int // The time that the grade was created
	timemodified int // The time that the grade was last updated
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
<summary>core_grades_grader_gradingpanel_scale_store</summary>
<br/>
<p>Store the data required to display the grader grading panel for scale-based grading</p>
<h3>Parameters</h3>
```
component string // The name of the component
contextid int // The ID of the context being graded
itemname string // The grade item itemname being graded
gradeduserid int // The ID of the user show
notifyuser int // Wheteher to notify the user or not
formdata string // The serialised form data representing the grade
```

<h3>Returns</h3>
```
templatename string // The template to use when rendering this data
hasgrade int // Does the user have a grade?
grade // 
{
	options // The description of the grade option
	[
		{
			value double // The grade value
			title string // The description fo the option
			selected int // Whether this item is currently selected
		}
	]
	usergrade string // Current user grade
	maxgrade string // Max possible grade
	gradedby string // The assumed grader of this grading instance
	timecreated int // The time that the grade was created
	timemodified int // The time that the grade was last updated
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
<summary>core_group_get_activity_allowed_groups</summary>
<br/>
<p>Gets a list of groups that the user is allowed to access within the specified activity.</p>
<h3>Parameters</h3>
```
cmid int // course module id
userid int // id of user, empty for current user
```

<h3>Returns</h3>
```
groups // 
[
	{
		id int // group record id
		name string // multilang compatible name, course unique
		description string // group description text
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		idnumber string // id number
		courseid int **Optional** // course id
	}
]
canaccessallgroups int **Optional** // Whether the user will be able to access all the activity groups.
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
<summary>core_group_get_activity_groupmode</summary>
<br/>
<p>Returns effective groupmode used in a given activity.</p>
<h3>Parameters</h3>
```
cmid int // course module id
```

<h3>Returns</h3>
```
groupmode int // group mode:
                                                    0 for no groups, 1 for separate groups, 2 for visible groups
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
<summary>core_group_get_course_groupings</summary>
<br/>
<p>Returns all groupings in specified course.</p>
<h3>Parameters</h3>
```
courseid int // id of course
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_group_get_course_groups</summary>
<br/>
<p>Returns all groups in specified course.</p>
<h3>Parameters</h3>
```
courseid int // id of course
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_group_get_course_user_groups</summary>
<br/>
<p>Returns all groups in specified course for the specified user.</p>
<h3>Parameters</h3>
```
courseid int // Id of course (empty or 0 for all the courses where the user is enrolled).
userid int // Id of user (empty or 0 for current user).
groupingid int // returns only groups in the specified grouping
```

<h3>Returns</h3>
```
groups // 
[
	{
		id int // group record id
		name string // multilang compatible name, course unique
		description string // group description text
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		idnumber string // id number
		courseid int **Optional** // course id
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
<summary>core_h5p_get_trusted_h5p_file</summary>
<br/>
<p>Get the H5P file cleaned for Mobile App.</p>
<h3>Parameters</h3>
```
url string // H5P file url.
frame int // The frame allow to show the bar options below the content
export int // The export allow to download the package
embed int // The embed allow to copy the code to your site
copyright int // The copyright option
```

<h3>Returns</h3>
```
files // H5P file trusted.
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
<summary>core_message_block_user</summary>
<br/>
<p>Blocks a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is blocking
blockeduserid int // The id of the user being blocked
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_confirm_contact_request</summary>
<br/>
<p>Confirms a contact request</p>
<h3>Parameters</h3>
```
userid int // The id of the user making the request
requesteduserid int // The id of the user being requested
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_create_contact_request</summary>
<br/>
<p>Creates a contact request</p>
<h3>Parameters</h3>
```
userid int // The id of the user making the request
requesteduserid int // The id of the user being requested
```

<h3>Returns</h3>
```
request **Optional** // request record
{
	id int // Message id
	userid int // User from id
	requesteduserid int // User to id
	timecreated int // Time created
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
<summary>core_message_data_for_messagearea_search_messages</summary>
<br/>
<p>Retrieve the template data for searching for messages</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is performing the search
search string // The string being searched
limitfrom int // Limit from
limitnum int // Limit number
```

<h3>Returns</h3>
```
contacts // 
[
	{
		userid int // The user's id
		fullname string // The user's name
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		ismessaging int // If we are messaging the user
		sentfromcurrentuser int // Was the last message sent from the current user?
		lastmessage string // The user's last message
		lastmessagedate int // Timestamp for last message
		messageid int // The unique search message id
		showonlinestatus int // Show the user's online status?
		isonline int // The user's online status
		isread int // If the user has read the message
		isblocked int // If the user has been blocked
		unreadcount int // The number of unread messages in this conversation
		conversationid int // The id of the conversation
	}
]
```

<hr/>
</details>
<details>
<summary>core_message_decline_contact_request</summary>
<br/>
<p>Declines a contact request</p>
<h3>Parameters</h3>
```
userid int // The id of the user making the request
requesteduserid int // The id of the user being requested
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_delete_contacts</summary>
<br/>
<p>Remove contacts from the contact list</p>
<h3>Parameters</h3>
```
userids // List of user IDs
[
	{
		int // User ID
	}
]
userid int // The id of the user we are deleting the contacts for, 0 for the
                    current user
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_delete_conversations_by_id</summary>
<br/>
<p>Deletes a list of conversations.</p>
<h3>Parameters</h3>
```
userid int // The user id of who we want to delete the conversation for
conversationids // List of conversation IDs
[
	{
		int // The id of the conversation
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_delete_message</summary>
<br/>
<p>Deletes a message.</p>
<h3>Parameters</h3>
```
messageid int // The message id
userid int // The user id of who we want to delete the message for
read int // If is a message read
```

<h3>Returns</h3>
```
status int // True if the message was deleted, false otherwise
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
<summary>core_message_delete_message_for_all_users</summary>
<br/>
<p>Deletes a message for all users.</p>
<h3>Parameters</h3>
```
messageid int // The message id
userid int // The user id of who we want to delete the message for all users
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_blocked_users</summary>
<br/>
<p>Retrieve a list of users blocked</p>
<h3>Parameters</h3>
```
userid int // the user whose blocked users we want to retrieve
```

<h3>Returns</h3>
```
users // List of blocked users
[
	{
		id int // User ID
		fullname string // User full name
		profileimageurl string **Optional** // User picture URL
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
<summary>core_message_get_contact_requests</summary>
<br/>
<p>Returns contact requests for a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user we want the requests for
limitfrom int // Limit from
limitnum int // Limit number
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_conversation</summary>
<br/>
<p>Retrieve a conversation for a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who we are viewing conversations for
conversationid int // The id of the conversation to fetch
includecontactrequests int // Include contact requests in the members
includeprivacyinfo int // Include privacy info in the members
memberlimit int // Limit for number of members
memberoffset int // Offset for member list
messagelimit int // Limit for number of messages
messageoffset int // Offset for messages list
newestmessagesfirst int // Order messages by newest first
```

<h3>Returns</h3>
```
id int // The conversation id
name string // The conversation name, if set
subname string // A subtitle for the conversation name, if set
imageurl string // A link to the conversation picture, if set
type int // The type of the conversation (1=individual,2=group,3=self)
membercount int // Total number of conversation members
ismuted int // If the user muted this conversation
isfavourite int // If the user marked this conversation as a favourite
isread int // If the user has read all messages in the conversation
unreadcount int // The number of unread messages in this conversation
members // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
messages // 
[
	{
		id int // The id of the message
		useridfrom int // The id of the user who sent the message
		text string // The text of the message
		timecreated int // The timecreated timestamp for the message
	}
]
candeletemessagesforallusers int // If the user can delete messages in the conversation for all users
```

<hr/>
</details>
<details>
<summary>core_message_get_conversations</summary>
<br/>
<p>Retrieve a list of conversations for a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who we are viewing conversations for
limitfrom int // The offset to start at
limitnum int // Limit number of conversations to this
type int // Filter by type
favourites int // Whether to restrict the results to contain NO favourite
                conversations (false), ONLY favourite conversation (true), or ignore any restriction altogether (null)
mergeself int // Whether to include self-conversations (true) or ONLY private
                    conversations (false) when private conversations are requested.
```

<h3>Returns</h3>
```
conversations // 
[
	{
		id int // The conversation id
		name string // The conversation name, if set
		subname string // A subtitle for the conversation name, if set
		imageurl string // A link to the conversation picture, if set
		type int // The type of the conversation (1=individual,2=group,3=self)
		membercount int // Total number of conversation members
		ismuted int // If the user muted this conversation
		isfavourite int // If the user marked this conversation as a favourite
		isread int // If the user has read all messages in the conversation
		unreadcount int // The number of unread messages in this conversation
		members // 
		[
			{
				id int // The user id
				fullname string // The user's name
				profileurl string // The link to the user's profile page
				profileimageurl string // User picture URL
				profileimageurlsmall string // Small user picture URL
				isonline int // The user's online status
				showonlinestatus int // Show the user's online status?
				isblocked int // If the user has been blocked
				iscontact int // Is the user a contact?
				isdeleted int // Is the user deleted?
				canmessageevenifblocked int // If the user can still message even if they get blocked
				canmessage int // If the user can be messaged
				requirescontact int // If the user requires to be contacts
				contactrequests **Optional** // The contact requests
				[
					{
						id int // The id of the contact request
						userid int // The id of the user who created the contact request
						requesteduserid int // The id of the user confirming the request
						timecreated int // The timecreated timestamp for the contact request
					}
				]
				conversations **Optional** // Conversations between users
				[
					{
						id int // Conversations id
						type int // Conversation type: private or public
						name string // Multilang compatible conversation name2
						timecreated int // The timecreated timestamp for the conversation
					}
				]
			}
		]
		messages // 
		[
			{
				id int // The id of the message
				useridfrom int // The id of the user who sent the message
				text string // The text of the message
				timecreated int // The timecreated timestamp for the message
			}
		]
		candeletemessagesforallusers int // If the user can delete messages in the conversation for all users
	}
]
```

<hr/>
</details>
<details>
<summary>core_message_get_conversation_between_users</summary>
<br/>
<p>Retrieve a conversation for a user between another user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who we are viewing conversations for
otheruserid int // The other user id
includecontactrequests int // Include contact requests in the members
includeprivacyinfo int // Include privacy info in the members
memberlimit int // Limit for number of members
memberoffset int // Offset for member list
messagelimit int // Limit for number of messages
messageoffset int // Offset for messages list
newestmessagesfirst int // Order messages by newest first
```

<h3>Returns</h3>
```
id int // The conversation id
name string // The conversation name, if set
subname string // A subtitle for the conversation name, if set
imageurl string // A link to the conversation picture, if set
type int // The type of the conversation (1=individual,2=group,3=self)
membercount int // Total number of conversation members
ismuted int // If the user muted this conversation
isfavourite int // If the user marked this conversation as a favourite
isread int // If the user has read all messages in the conversation
unreadcount int // The number of unread messages in this conversation
members // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
messages // 
[
	{
		id int // The id of the message
		useridfrom int // The id of the user who sent the message
		text string // The text of the message
		timecreated int // The timecreated timestamp for the message
	}
]
candeletemessagesforallusers int // If the user can delete messages in the conversation for all users
```

<hr/>
</details>
<details>
<summary>core_message_get_conversation_counts</summary>
<br/>
<p>Retrieve a list of conversation counts, indexed by type.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
```

<h3>Returns</h3>
```
favourites int // Total number of favourite conversations
types // 
{
	1 int // Total number of individual conversations
	2 int // Total number of group conversations
	3 int // Total number of self conversations
}
```

<hr/>
</details>
<details>
<summary>core_message_get_conversation_members</summary>
<br/>
<p>Retrieve a list of members in a conversation</p>
<h3>Parameters</h3>
```
userid int // The id of the user we are performing this action on behalf of
conversationid int // The id of the conversation
includecontactrequests int // Do we want to include contact requests?
includeprivacyinfo int // Do we want to include privacy info?
limitfrom int // Limit from
limitnum int // Limit number
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_conversation_messages</summary>
<br/>
<p>Retrieve the conversation messages and relevant member information</p>
<h3>Parameters</h3>
```
currentuserid int // The current user's id
convid int // The conversation id
limitfrom int // Limit from
limitnum int // Limit number
newest int // Newest first?
timefrom int // The timestamp from which the messages were created
```

<h3>Returns</h3>
```
id int // The conversation id
members // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
messages // 
[
	{
		id int // The id of the message
		useridfrom int // The id of the user who sent the message
		text string // The text of the message
		timecreated int // The timecreated timestamp for the message
	}
]
```

<hr/>
</details>
<details>
<summary>core_message_get_member_info</summary>
<br/>
<p>Retrieve a user message profiles</p>
<h3>Parameters</h3>
```
referenceuserid int // id of the user
userids // 
[
	{
		int // id of members to get
	}
]
includecontactrequests int // include contact requests in response
includeprivacyinfo int // include privacy info in response
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_messages</summary>
<br/>
<p>Retrieve a list of messages sent and received by a user (conversations, notifications or both)</p>
<h3>Parameters</h3>
```
useridto int // the user id who received the message, 0 for any user
useridfrom int // the user id who send the message, 0 for any user. -10 or -20 for no-reply or support user
type string // type of message to return, expected values are: notifications, conversations and both
read int // true for getting read messages, false for unread
newestfirst int // true for ordering by newest first, false for oldest first
limitfrom int // limit from
limitnum int // limit number
```

<h3>Returns</h3>
```
messages // 
[
	{
		id int // Message id
		useridfrom int // User from id
		useridto int // User to id
		subject string // The message subject
		text string // The message text formated
		fullmessage string // The message
		fullmessageformat int // fullmessage format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		fullmessagehtml string // The message in html
		smallmessage string // The shorten message
		notification int // Is a notification?
		contexturl string // Context URL
		contexturlname string // Context URL link name
		timecreated int // Time created
		timeread int // Time read
		usertofullname string // User to full name
		userfromfullname string // User from full name
		component string **Optional** // The component that generated the notification
		eventtype string **Optional** // The type of notification
		customdata string **Optional** // Custom data to be passed to the message processor.
                                The data here is serialised using json_encode().
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
<summary>core_message_get_received_contact_requests_count</summary>
<br/>
<p>Gets the number of received contact requests</p>
<h3>Parameters</h3>
```
userid int // The id of the user we want to return the number of received contact requests for
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_self_conversation</summary>
<br/>
<p>Retrieve a self-conversation for a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who we are viewing self-conversations for
messagelimit int // Limit for number of messages
messageoffset int // Offset for messages list
newestmessagesfirst int // Order messages by newest first
```

<h3>Returns</h3>
```
id int // The conversation id
name string // The conversation name, if set
subname string // A subtitle for the conversation name, if set
imageurl string // A link to the conversation picture, if set
type int // The type of the conversation (1=individual,2=group,3=self)
membercount int // Total number of conversation members
ismuted int // If the user muted this conversation
isfavourite int // If the user marked this conversation as a favourite
isread int // If the user has read all messages in the conversation
unreadcount int // The number of unread messages in this conversation
members // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
messages // 
[
	{
		id int // The id of the message
		useridfrom int // The id of the user who sent the message
		text string // The text of the message
		timecreated int // The timecreated timestamp for the message
	}
]
candeletemessagesforallusers int // If the user can delete messages in the conversation for all users
```

<hr/>
</details>
<details>
<summary>core_message_get_unread_conversations_count</summary>
<br/>
<p>Retrieve the count of unread conversations for a given user</p>
<h3>Parameters</h3>
```
useridto int // the user id who received the message, 0 for any user
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_unread_conversation_counts</summary>
<br/>
<p>Retrieve a list of unread conversation counts, indexed by type.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
```

<h3>Returns</h3>
```
favourites int // Total number of unread favourite conversations
types // 
{
	1 int // Total number of unread individual conversations
	2 int // Total number of unread group conversations
	3 int // Total number of unread self conversations
}
```

<hr/>
</details>
<details>
<summary>core_message_get_user_contacts</summary>
<br/>
<p>Retrieve the contact list</p>
<h3>Parameters</h3>
```
userid int // The id of the user who we retrieving the contacts for
limitfrom int // Limit from
limitnum int // Limit number
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_get_user_message_preferences</summary>
<br/>
<p>Get the message preferences for a given user.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
```

<h3>Returns</h3>
```
preferences // 
{
	userid int // User id
	disableall int // Whether all the preferences are disabled
	processors // Config form values
	[
		{
			displayname string // Display name
			name string // Processor name
			hassettings int // Whether has settings
			contextid int // Context id
			userconfigured int // Whether is configured by the user
		}
	]
	components // Available components
	[
		{
			displayname string // Display name
			notifications // List of notificaitons for the component
			[
				{
					displayname string // Display name
					preferencekey string // Preference key
					processors // Processors values for this notification
					[
						{
							displayname string // Display name
							name string // Processor name
							locked int // Is locked by admin?
							lockedmessage string **Optional** // Text to display if locked
							userconfigured int // Is configured?
							loggedin // 
							{
								name string // Name
								displayname string // Display name
								checked int // Is checked?
							}
							loggedoff // 
							{
								name string // Name
								displayname string // Display name
								checked int // Is checked?
							}
						}
					]
				}
			]
		}
	]
}
blocknoncontacts int // Privacy messaging setting to define who can message you
entertosend int // User preference for using enter to send messages
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
<summary>core_message_get_user_notification_preferences</summary>
<br/>
<p>Get the notification preferences for a given user.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
```

<h3>Returns</h3>
```
preferences // 
{
	userid int // User id
	disableall int // Whether all the preferences are disabled
	processors // Config form values
	[
		{
			displayname string // Display name
			name string // Processor name
			hassettings int // Whether has settings
			contextid int // Context id
			userconfigured int // Whether is configured by the user
		}
	]
	components // Available components
	[
		{
			displayname string // Display name
			notifications // List of notificaitons for the component
			[
				{
					displayname string // Display name
					preferencekey string // Preference key
					processors // Processors values for this notification
					[
						{
							displayname string // Display name
							name string // Processor name
							locked int // Is locked by admin?
							lockedmessage string **Optional** // Text to display if locked
							userconfigured int // Is configured?
							loggedin // 
							{
								name string // Name
								displayname string // Display name
								checked int // Is checked?
							}
							loggedoff // 
							{
								name string // Name
								displayname string // Display name
								checked int // Is checked?
							}
						}
					]
				}
			]
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
<summary>core_message_mark_all_conversation_messages_as_read</summary>
<br/>
<p>Mark all conversation messages as read for a given user</p>
<h3>Parameters</h3>
```
userid int // The user id who who we are marking the messages as read for
conversationid int // The conversation id who who we are marking the messages as read for
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_mark_all_notifications_as_read</summary>
<br/>
<p>Mark all notifications as read for a given user</p>
<h3>Parameters</h3>
```
useridto int // the user id who received the message, 0 for any user
useridfrom int // the user id who send the message, 0 for any user. -10 or -20 for no-reply or support user
timecreatedto int // mark messages created before this time as read, 0 for all messages
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_mark_message_read</summary>
<br/>
<p>Mark a single message as read, trigger message_viewed event.</p>
<h3>Parameters</h3>
```
messageid int // id of the message in the messages table
timeread int // timestamp for when the message should be marked read
```

<h3>Returns</h3>
```
messageid int // the id of the message in the messages table
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
<summary>core_message_mark_notification_read</summary>
<br/>
<p>Mark a single notification as read, trigger notification_viewed event.</p>
<h3>Parameters</h3>
```
notificationid int // id of the notification
timeread int // timestamp for when the notification should be marked read
```

<h3>Returns</h3>
```
notificationid int // id of the notification
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
<summary>core_message_message_processor_config_form</summary>
<br/>
<p>Process the message processor config form</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
name string // The name of the message processor
formvalues // Config form values
[
	{
		name string // name of the form element
		value string // value of the form element
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_message_search_users</summary>
<br/>
<p>Retrieve the data for searching for people</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is performing the search
search string // The string being searched
limitfrom int // Limit from
limitnum int // Limit number
```

<h3>Returns</h3>
```
contacts // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
noncontacts // 
[
	{
		id int // The user id
		fullname string // The user's name
		profileurl string // The link to the user's profile page
		profileimageurl string // User picture URL
		profileimageurlsmall string // Small user picture URL
		isonline int // The user's online status
		showonlinestatus int // Show the user's online status?
		isblocked int // If the user has been blocked
		iscontact int // Is the user a contact?
		isdeleted int // Is the user deleted?
		canmessageevenifblocked int // If the user can still message even if they get blocked
		canmessage int // If the user can be messaged
		requirescontact int // If the user requires to be contacts
		contactrequests **Optional** // The contact requests
		[
			{
				id int // The id of the contact request
				userid int // The id of the user who created the contact request
				requesteduserid int // The id of the user confirming the request
				timecreated int // The timecreated timestamp for the contact request
			}
		]
		conversations **Optional** // Conversations between users
		[
			{
				id int // Conversations id
				type int // Conversation type: private or public
				name string // Multilang compatible conversation name2
				timecreated int // The timecreated timestamp for the conversation
			}
		]
	}
]
```

<hr/>
</details>
<details>
<summary>core_message_mute_conversations</summary>
<br/>
<p>Mutes a list of conversations</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is blocking
conversationids // 
[
	{
		int // id of the conversation
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_search_contacts</summary>
<br/>
<p>Search for contacts</p>
<h3>Parameters</h3>
```
searchtext string // String the user's fullname has to match to be found
onlymycourses int // Limit search to the user's courses
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_send_instant_messages</summary>
<br/>
<p>Send instant messages</p>
<h3>Parameters</h3>
```
messages // 
[
	{
		touserid int // id of the user to send the private message
		text string // the text of the message
		textformat int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		clientmsgid string **Optional** // your own client id for the message. If this id is provided, the fail message id will be returned to you
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_send_messages_to_conversation</summary>
<br/>
<p>Send messages to an existing conversation between users</p>
<h3>Parameters</h3>
```
conversationid int // id of the conversation
messages // 
[
	{
		text string // the text of the message
		textformat int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_set_favourite_conversations</summary>
<br/>
<p>Mark a conversation or group of conversations as favourites/starred conversations.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
conversations // 
[
	{
		int // id of the conversation
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_unblock_user</summary>
<br/>
<p>Unblocks a user</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is unblocking
unblockeduserid int // The id of the user being unblocked
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_unmute_conversations</summary>
<br/>
<p>Unmutes a list of conversations</p>
<h3>Parameters</h3>
```
userid int // The id of the user who is unblocking
conversationids // 
[
	{
		int // id of the conversation
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_message_unset_favourite_conversations</summary>
<br/>
<p>Unset a conversation or group of conversations as favourites/starred conversations.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
conversations // 
[
	{
		int // id of the conversation
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_notes_create_notes</summary>
<br/>
<p>Create notes</p>
<h3>Parameters</h3>
```
notes // 
[
	{
		userid int // id of the user the note is about
		publishstate string // 'personal', 'course' or 'site'
		courseid int // course id of the note (in Moodle a note can only be created into a course, even for site and personal notes)
		text string // the text of the message - text or HTML
		format int // text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		clientnoteid string **Optional** // your own client id for the note. If this id is provided, the fail message id will be returned to you
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_notes_delete_notes</summary>
<br/>
<p>Delete notes</p>
<h3>Parameters</h3>
```
notes // Array of Note Ids to be deleted.
[
	{
		int // ID of the note to be deleted
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_notes_get_course_notes</summary>
<br/>
<p>Returns all notes in specified course (or site), for the specified user.</p>
<h3>Parameters</h3>
```
courseid int // course id, 0 for SITE
userid int // user id
```

<h3>Returns</h3>
```
sitenotes **Optional** // site notes
[
	{
		id int // id of this note
		courseid int // id of the course
		userid int // user id
		content string // the content text formated
		format int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		created int // time created (timestamp)
		lastmodified int // time of last modification (timestamp)
		usermodified int // user id of the creator of this note
		publishstate string // state of the note (i.e. draft, public, site) 
	}
]
coursenotes **Optional** // couse notes
[
	{
		id int // id of this note
		courseid int // id of the course
		userid int // user id
		content string // the content text formated
		format int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		created int // time created (timestamp)
		lastmodified int // time of last modification (timestamp)
		usermodified int // user id of the creator of this note
		publishstate string // state of the note (i.e. draft, public, site) 
	}
]
personalnotes **Optional** // personal notes
[
	{
		id int // id of this note
		courseid int // id of the course
		userid int // user id
		content string // the content text formated
		format int // content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		created int // time created (timestamp)
		lastmodified int // time of last modification (timestamp)
		usermodified int // user id of the creator of this note
		publishstate string // state of the note (i.e. draft, public, site) 
	}
]
canmanagesystemnotes int **Optional** // Whether the user can manage notes at system level.
canmanagecoursenotes int **Optional** // Whether the user can manage notes at the given course.
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
<summary>core_notes_view_notes</summary>
<br/>
<p>Simulates the web interface view of notes/index.php: trigger events.</p>
<h3>Parameters</h3>
```
courseid int // course id, 0 for notes at system level
userid int // user id, 0 means view all the user notes
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_question_update_flag</summary>
<br/>
<p>Update the flag state of a question attempt.</p>
<h3>Parameters</h3>
```
qubaid int // the question usage id.
questionid int // the question id
qaid int // the question_attempt id
slot int // the slot number within the usage
checksum string // computed checksum with the last three arguments and
                             the users username
newstate int // the new state of the flag. true = flagged
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_rating_add_rating</summary>
<br/>
<p>Rates an item.</p>
<h3>Parameters</h3>
```
contextlevel string // context level: course, module, user, etc...
instanceid int // the instance id of item associated with the context level
component string // component
ratingarea string // rating area
itemid int // associated id
scaleid int // scale id
rating int // user rating
rateduserid int // rated user id
aggregation int // agreggation method
```

<h3>Returns</h3>
```
success int // Whether the rate was successfully created
aggregate string **Optional** // New aggregate
count int **Optional** // Ratings count
itemid int **Optional** // Rating item id
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
<summary>core_rating_get_item_ratings</summary>
<br/>
<p>Retrieve all the ratings for an item.</p>
<h3>Parameters</h3>
```
contextlevel string // context level: course, module, user, etc...
instanceid int // the instance id of item associated with the context level
component string // component
ratingarea string // rating area
itemid int // associated id
scaleid int // scale id
sort string // sort order (firstname, rating or timemodified)
```

<h3>Returns</h3>
```
ratings // list of ratings
[
	{
		id int // rating id
		userid int // user id
		userpictureurl string // URL user picture
		userfullname string // user fullname
		rating string // rating on scale
		timemodified int // time modified (timestamp)
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
<summary>core_table_get_dynamic_table_content</summary>
<br/>
<p>Get the dynamic table content raw html</p>
<h3>Parameters</h3>
```
component string // Component
handler string // Handler
uniqueid string // Unique ID for the container
sortdata **Optional** // The combined sort order of the table. Multiple fields can be specified.
[
	{
		sortby string // The name of a sortable column
		sortorder string // The direction that this column should be sorted by
	}
]
filters **Optional** // The filters that will be applied in the request
[
	{
		name string // Name of the filter
		jointype int // Type of join for filter values
		values // The value to filter on
		[
			{
		string // Filter value
			}
		]
	}
]
jointype int // Type of join to join all filters together
firstinitial string // The first initial to sort filter on
lastinitial string // The last initial to sort filter on
pagenumber int // The page number
pagesize int // The number of records per page
hiddencolumns // 
[
	{
		string // Name of column
	}
]
resetpreferences int // Whether the table preferences should be reset
```

<h3>Returns</h3>
```
html string // The raw html of the requested table.
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
<summary>core_tag_get_tagindex</summary>
<br/>
<p>Gets tag index page for one tag and one tag area</p>
<h3>Parameters</h3>
```
tagindex // parameters
{
	tag string // tag name
	tc int // tag collection id
	ta int // tag area id
	excl int **Optional** // exlusive mode for this tag area
	from int **Optional** // context id where the link was displayed
	ctx int **Optional** // context id where to search for items
	rec int **Optional** // search in the context recursive
	page int **Optional** // page number (0-based)
}
```

<h3>Returns</h3>
```
tagid int // tag id
ta int // tag area id
component string // component
itemtype string // itemtype
nextpageurl string **Optional** // URL for the next page
prevpageurl string **Optional** // URL for the next page
exclusiveurl string **Optional** // URL for exclusive link
exclusivetext string **Optional** // text for exclusive link
title string // title
content string // title
hascontent int // whether the content is present
anchor string **Optional** // name of anchor
```

<hr/>
</details>
<details>
<summary>core_tag_get_tagindex_per_area</summary>
<br/>
<p>Gets tag index page per different areas.</p>
<h3>Parameters</h3>
```
tagindex // parameters
{
	id int **Optional** // tag id
	tag string **Optional** // tag name
	tc int **Optional** // tag collection id
	ta int **Optional** // tag area id
	excl int **Optional** // exlusive mode for this tag area
	from int **Optional** // context id where the link was displayed
	ctx int **Optional** // context id where to search for items
	rec int **Optional** // search in the context recursive
	page int **Optional** // page number (0-based)
}
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_tag_get_tag_areas</summary>
<br/>
<p>Retrieves existing tag areas.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
areas // 
[
	{
		id int // Area id.
		component string // Component the area is related to.
		itemtype string // Type of item in the component.
		enabled int // Whether this area is enabled.
		tagcollid int // The tag collection this are belongs to.
		callback string // Component callback for processing tags.
		callbackfile string // Component callback file.
		showstandard int // Return whether to display only standard, only non-standard or both tags.
		multiplecontexts int // Whether the tag area allows tag instances to be created in multiple contexts. 
		locked int **Optional** // Whether the area is locked.
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
<summary>core_tag_get_tag_cloud</summary>
<br/>
<p>Retrieves a tag cloud for the given collection and/or query search.</p>
<h3>Parameters</h3>
```
tagcollid int // Tag collection id.
isstandard int // Whether to return only standard tags.
limit int // Maximum number of tags to retrieve.
sort string // Sort order for display
                    (id, name, rawname, count, flag, isstandard, tagcollid).
search string // Search string.
fromctx int // Context id where this tag cloud is displayed.
ctx int // Only retrieve tag instances in this context.
rec int // Retrieve tag instances in the $ctx context and it's children.
```

<h3>Returns</h3>
```
tags // 
[
	{
		name string // Tag name.
		viewurl string // URL to view the tag index.
		flag int **Optional** // Whether the tag is flagged as inappropriate.
		isstandard int **Optional** // Whether is a standard tag or not.
		count int **Optional** // Number of tag instances.
		size int **Optional** // Proportional size to display the tag.
	}
]
tagscount int // Number of tags returned.
totalcount int // Total count of tags.
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
<summary>core_tag_get_tag_collections</summary>
<br/>
<p>Retrieves existing tag collections.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
collections // 
[
	{
		id int // Collection id.
		name string // Collection name.
		isdefault int // Whether is the default collection.
		component string // Component the collection is related to.
		sortorder int // Collection ordering in the list.
		searchable int // Whether the tag collection is searchable.
		customurl string // Custom URL for the tag page instead of /tag/index.php.
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
<summary>core_user_add_user_device</summary>
<br/>
<p>Store mobile user devices information for PUSH Notifications.</p>
<h3>Parameters</h3>
```
appid string // the app id, usually something like com.moodle.moodlemobile
name string // the device name, 'occam' or 'iPhone' etc.
model string // the device model 'Nexus4' or 'iPad1,1' etc.
platform string // the device platform 'iOS' or 'Android' etc.
version string // the device version '6.1.2' or '4.2.2' etc.
pushid string // the device PUSH token/key/identifier/registration id
uuid string // the device UUID
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_user_add_user_private_files</summary>
<br/>
<p>Copy files from a draft area to users private files area.</p>
<h3>Parameters</h3>
```
draftid int // draft area id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_user_agree_site_policy</summary>
<br/>
<p>Agree the site policy for the current user.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
status int // Status: true only if we set the policyagreed to 1 for the user
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
<summary>core_user_get_course_user_profiles</summary>
<br/>
<p>Get course user profiles (each of the profils matching a course id and a user id),.</p>
<h3>Parameters</h3>
```
userlist // 
[
	{
		userid int // userid
		courseid int // courseid
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_user_get_private_files_info</summary>
<br/>
<p>Returns general information about files in the user private files area.</p>
<h3>Parameters</h3>
```
userid int // Id of the user, default to current user.
```

<h3>Returns</h3>
```
filecount int // Number of files in the area.
foldercount int // Number of folders in the area.
filesize int // Total size of the files in the area.
filesizewithoutreferences int // Total size of the area excluding file references
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
<summary>core_user_get_users_by_field</summary>
<br/>
<p>Retrieve users' information for a specified unique field - If you want to do a user search, use core_user_get_users()</p>
<h3>Parameters</h3>
```
field string // the search field can be
                    'id' or 'idnumber' or 'username' or 'email'
values // 
[
	{
		string // the value to match
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_user_get_user_preferences</summary>
<br/>
<p>Return user preferences.</p>
<h3>Parameters</h3>
```
name string // preference name, empty for all
userid int // id of the user, default to current user
```

<h3>Returns</h3>
```
preferences // User custom fields (also known as user profile fields)
[
	{
		name string // The name of the preference
		value string // The value of the preference
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
<summary>core_user_remove_user_device</summary>
<br/>
<p>Remove a user device from the Moodle database.</p>
<h3>Parameters</h3>
```
uuid string // the device UUID
appid string // the app id, if empty devices matching the UUID for the user will be removed
```

<h3>Returns</h3>
```
removed int // True if removed, false if not removed because it doesn't exists
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
<summary>core_user_set_user_preferences</summary>
<br/>
<p>Set user preferences.</p>
<h3>Parameters</h3>
```
preferences // 
[
	{
		name string // The name of the preference
		value string // The value of the preference
		userid int // Id of the user to set the preference
	}
]
```

<h3>Returns</h3>
```
saved // Preferences saved
[
	{
		name string // The name of the preference
		userid int // The user the preference was set for
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
<summary>core_user_update_picture</summary>
<br/>
<p>Update or delete the user picture in the site</p>
<h3>Parameters</h3>
```
draftitemid int // Id of the user draft file to use as image
delete int // If we should delete the user picture
userid int // Id of the user, 0 for current user
```

<h3>Returns</h3>
```
success int // True if the image was updated, false otherwise.
profileimageurl string **Optional** // New profile user image url
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
<summary>core_user_update_user_preferences</summary>
<br/>
<p>Update a user's preferences</p>
<h3>Parameters</h3>
```
userid int // id of the user, default to current user
emailstop int // Enable or disable notifications for this user
preferences // User preferences
[
	{
		type string // The name of the preference
		value string // The value of the preference, do not set this field if you
                                want to remove (unset) the current value.
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>core_user_view_user_list</summary>
<br/>
<p>Simulates the web-interface view of user/index.php (triggering events),.</p>
<h3>Parameters</h3>
```
courseid int // id of the course, 0 for site
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_user_view_user_profile</summary>
<br/>
<p>Simulates the web-interface view of user/view.php and user/profile.php (triggering events),.</p>
<h3>Parameters</h3>
```
userid int // id of the user, 0 for current user
courseid int // id of the course, default site course
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>core_webservice_get_site_info</summary>
<br/>
<p>Return some site info / user info / list web service functions</p>
<h3>Parameters</h3>
```
serviceshortnames // DEPRECATED PARAMETER - it was a design error in the original implementation. \
                    It is ignored now. (parameter kept for backward compatibility)
[
	{
		string // service shortname
	}
]
```

<h3>Returns</h3>
```
sitename string // site name
username string // username
firstname string // first name
lastname string // last name
fullname string // user full name
lang string // Current language.
userid int // user id
siteurl string // site url
userpictureurl string // the user profile picture.
                    Warning: this url is the public URL that only works when forcelogin is set to NO and guestaccess is set to YES.
                    In order to retrieve user profile pictures independently of the Moodle config, replace "pluginfile.php" by
                    "webservice/pluginfile.php?token=WSTOKEN&file="
                    Of course the user can only see profile picture depending
                    on his/her permissions. Moreover it is recommended to use HTTPS too.
functions // 
[
	{
		name string // function name
		version string // The version number of the component to which the function belongs
	}
]
downloadfiles int **Optional** // 1 if users are allowed to download files, 0 if not
uploadfiles int **Optional** // 1 if users are allowed to upload files, 0 if not
release string **Optional** // Moodle release number
version string **Optional** // Moodle version number
mobilecssurl string **Optional** // Mobile custom CSS theme
advancedfeatures **Optional** // Advanced features availability
[
	{
		name string // feature name
		value int // feature value. Usually 1 means enabled.
	}
]
usercanmanageownfiles int **Optional** // true if the user can manage his own files
userquota int **Optional** // user quota (bytes). 0 means user can ignore the quota
usermaxuploadfilesize int **Optional** // user max upload file size (bytes). -1 means the user can ignore the upload file size
userhomepage int **Optional** // the default home page for the user: 0 for the site home, 1 for dashboard
userprivateaccesskey string **Optional** // Private user access key for fetching files.
siteid int **Optional** // Site course ID
sitecalendartype string **Optional** // Calendar type set in the site.
usercalendartype string **Optional** // Calendar typed used by the user.
userissiteadmin int **Optional** // Whether the user is a site admin or not.
theme string **Optional** // Current theme for the user.
```

<hr/>
</details>
<details>
<summary>core_xapi_statement_post</summary>
<br/>
<p>Post an xAPI statement.</p>
<h3>Parameters</h3>
```
component string // Component name
requestjson string // json object with all the statements to post
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>enrol_guest_get_instance_info</summary>
<br/>
<p>Return guest enrolment instance information.</p>
<h3>Parameters</h3>
```
instanceid int // Instance id of guest enrolment plugin.
```

<h3>Returns</h3>
```
instanceinfo // 
{
	id int // Id of course enrolment instance
	courseid int // Id of course
	type string // Type of enrolment plugin
	name string // Name of enrolment plugin
	status int // Is the enrolment enabled?
	passwordrequired int // Is a password required?
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
<summary>enrol_self_enrol_user</summary>
<br/>
<p>Self enrol the current user in the given course.</p>
<h3>Parameters</h3>
```
courseid int // Id of the course
password string // Enrolment key
instanceid int // Instance id of self enrolment plugin.
```

<h3>Returns</h3>
```
status int // status: true if the user is enrolled, false otherwise
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
<summary>enrol_self_get_instance_info</summary>
<br/>
<p>self enrolment instance information.</p>
<h3>Parameters</h3>
```
instanceid int // instance id of self enrolment plugin.
```

<h3>Returns</h3>
```
id int // id of course enrolment instance
courseid int // id of course
type string // type of enrolment plugin
name string // name of enrolment plugin
status string // status of enrolment plugin
enrolpassword string **Optional** // password required for enrolment
```

<hr/>
</details>
<details>
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
<summary>gradereport_overview_view_grade_report</summary>
<br/>
<p>Trigger the report view event</p>
<h3>Parameters</h3>
```
courseid int // id of the course
userid int // id of the user, 0 means current user
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>gradereport_user_view_grade_report</summary>
<br/>
<p>Trigger the report view event</p>
<h3>Parameters</h3>
```
courseid int // id of the course
userid int // id of the user, 0 means current user
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>message_airnotifier_are_notification_preferences_configured</summary>
<br/>
<p>Check if the users have notification preferences configured yet</p>
<h3>Parameters</h3>
```
userids // 
[
	{
		int // user ID
	}
]
```

<h3>Returns</h3>
```
users // list of preferences by user
[
	{
		userid int // userid id
		configured int // 1 if the user preferences have been configured and 0 if not
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
<summary>message_airnotifier_enable_device</summary>
<br/>
<p>Enables or disables a registered user device so it can receive Push notifications</p>
<h3>Parameters</h3>
```
deviceid int // The device id
enable int // True for enable the device, false otherwise
```

<h3>Returns</h3>
```
success int // True if success
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
<summary>message_airnotifier_get_user_devices</summary>
<br/>
<p>Return the list of mobile devices that are registered in Moodle for the given user</p>
<h3>Parameters</h3>
```
appid string // App unique id (usually a reversed domain)
userid int // User id, 0 for current user
```

<h3>Returns</h3>
```
devices // List of devices
[
	{
		id int // Device id (in the message_airnotifier table)
		appid string // The app id, something like com.moodle.moodlemobile
		name string // The device name, 'occam' or 'iPhone' etc.
		model string // The device model 'Nexus4' or 'iPad1,1' etc.
		platform string // The device platform 'iOS' or 'Android' etc.
		version string // The device version '6.1.2' or '4.2.2' etc.
		pushid string // The device PUSH token/key/identifier/registration id
		uuid string // The device UUID
		enable int // Whether the device is enabled or not
		timecreated int // Time created
		timemodified int // Time modified
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
<summary>message_airnotifier_is_system_configured</summary>
<br/>
<p>Check whether the airnotifier settings have been configured</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>message_popup_get_popup_notifications</summary>
<br/>
<p>Retrieve a list of popup notifications for a user</p>
<h3>Parameters</h3>
```
useridto int // the user id who received the message, 0 for current user
newestfirst int // true for ordering by newest first, false for oldest first
limit int // the number of results to return
offset int // offset the result set by a given amount
```

<h3>Returns</h3>
```
notifications // 
[
	{
		id int // Notification id (this is not guaranteed to be unique
                                within this result set)
		useridfrom int // User from id
		useridto int // User to id
		subject string // The notification subject
		shortenedsubject string // The notification subject shortened
                                with ellipsis
		text string // The message text formated
		fullmessage string // The message
		fullmessageformat int // fullmessage format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		fullmessagehtml string // The message in html
		smallmessage string // The shorten message
		contexturl string // Context URL
		contexturlname string // Context URL link name
		timecreated int // Time created
		timecreatedpretty string // Time created in a pretty format
		timeread int // Time read
		read int // notification read status
		deleted int // notification deletion status
		iconurl string // URL for notification icon
		component string **Optional** // The component that generated the notification
		eventtype string **Optional** // The type of notification
		customdata string **Optional** // Custom data to be passed to the message processor.
                                The data here is serialised using json_encode().
	}
]
unreadcount int // the number of unread message for the given user
```

<hr/>
</details>
<details>
<summary>message_popup_get_unread_popup_notification_count</summary>
<br/>
<p>Retrieve the count of unread popup notifications for a given user</p>
<h3>Parameters</h3>
```
useridto int // the user id who received the message, 0 for any user
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
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
<summary>mod_assign_get_grades</summary>
<br/>
<p>Returns grades from the assignment</p>
<h3>Parameters</h3>
```
assignmentids // 1 or more assignment ids
[
	{
		int // assignment id
	}
]
since int // timestamp, only return records where timemodified >= since
```

<h3>Returns</h3>
```
assignments // list of assignment grade information
[
	{
		assignmentid int // assignment id
		grades // 
		[
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
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item is always 'assignment'
		itemid int **Optional** // when errorcode is 3 then itemid is an assignment id. When errorcode is 1, itemid is a course module id
		warningcode string // errorcode can be 3 (no grades found) or 1 (no permission to get grades)
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_assign_get_participant</summary>
<br/>
<p>Get a participant for an assignment, with some summary info about their submissions.</p>
<h3>Parameters</h3>
```
assignid int // assign instance id
userid int // user id
embeduser int // user id
```

<h3>Returns</h3>
```
id int // ID of the user
fullname string // The fullname of the user
submitted int // have they submitted their assignment
requiregrading int // is their submission waiting for grading
grantedextension int // have they been granted an extension
blindmarking int // is blind marking enabled for this assignment
allowsubmissionsfromdate int // allowsubmissionsfromdate for the user
duedate int // duedate for the user
cutoffdate int // cutoffdate for the user
duedatestr string // duedate for the user
groupid int **Optional** // for group assignments this is the group id
groupname string **Optional** // for group assignments this is the group name
user **Optional** // 
{
	id int // ID of the user
	username string **Optional** // The username
	firstname string **Optional** // The first name(s) of the user
	lastname string **Optional** // The family name of the user
	fullname string // The fullname of the user
	email string **Optional** // An email address - allow email as root@localhost
	address string **Optional** // Postal address
	phone1 string **Optional** // Phone 1
	phone2 string **Optional** // Phone 2
	icq string **Optional** // icq number
	skype string **Optional** // skype id
	yahoo string **Optional** // yahoo id
	aim string **Optional** // aim id
	msn string **Optional** // msn number
	department string **Optional** // department
	institution string **Optional** // institution
	idnumber string **Optional** // An arbitrary ID code number perhaps from the institution
	interests string **Optional** // user interests (separated by commas)
	firstaccess int **Optional** // first access to the site (0 if never)
	lastaccess int **Optional** // last access to the site (0 if never)
	auth string **Optional** // Auth plugins include manual, ldap, etc
	suspended int **Optional** // Suspend user account, either false to enable user login or true to disable it
	confirmed int **Optional** // Active user: 1 if confirmed, 0 otherwise
	lang string **Optional** // Language code such as "en", must exist on server
	calendartype string **Optional** // Calendar type such as "gregorian", must exist on server
	theme string **Optional** // Theme name such as "standard", must exist on server
	timezone string **Optional** // Timezone code such as Australia/Perth, or 99 for default
	mailformat int **Optional** // Mail format code is 0 for plain text, 1 for HTML etc
	description string **Optional** // User profile description
	descriptionformat int **Optional** // int format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	city string **Optional** // Home city of the user
	url string **Optional** // URL of the user
	country string **Optional** // Home country code of the user, such as AU or CZ
	profileimageurlsmall string // User image profile URL - small version
	profileimageurl string // User image profile URL - big version
	customfields **Optional** // User custom fields (also known as user profile fields)
	[
		{
			type string // The type of the custom field - text field, checkbox...
			value string // The value of the custom field
			name string // The name of the custom field
			shortname string // The shortname of the custom field - to be able to build the field class in the code
		}
	]
	preferences **Optional** // Users preferences
	[
		{
			name string // The name of the preferences
			value string // The value of the preference
		}
	]
}
```

<hr/>
</details>
<details>
<summary>mod_assign_get_submissions</summary>
<br/>
<p>Returns the submissions for assignments</p>
<h3>Parameters</h3>
```
assignmentids // 1 or more assignment ids
[
	{
		int // assignment id
	}
]
status string // status
since int // submitted since
before int // submitted before
```

<h3>Returns</h3>
```
assignments // assignment submissions
[
	{
		assignmentid int // assignment id
		submissions // 
		[
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
<summary>mod_assign_get_user_flags</summary>
<br/>
<p>Returns the user flags for assignments</p>
<h3>Parameters</h3>
```
assignmentids // 1 or more assignment ids
[
	{
		int // assignment id
	}
]
```

<h3>Returns</h3>
```
assignments // list of assign user flag information
[
	{
		assignmentid int // assignment id
		userflags // 
		[
			{
				id int // user flag id
				userid int // student id
				locked int // locked
				mailed int // mailed
				extensionduedate int // extension due date
				workflowstate string **Optional** // marking workflow state
				allocatedmarker int // allocated marker
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item is always 'assignment'
		itemid int **Optional** // when errorcode is 3 then itemid is an assignment id. When errorcode is 1, itemid is a course module id
		warningcode string // errorcode can be 3 (no user flags found) or 1 (no permission to get user flags)
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_assign_get_user_mappings</summary>
<br/>
<p>Returns the blind marking mappings for assignments</p>
<h3>Parameters</h3>
```
assignmentids // 1 or more assignment ids
[
	{
		int // assignment id
	}
]
```

<h3>Returns</h3>
```
assignments // list of assign user mapping data
[
	{
		assignmentid int // assignment id
		mappings // 
		[
			{
				id int // user mapping id
				userid int // student id
			}
		]
	}
]
warnings **Optional** // list of warnings
[
	{
		item string **Optional** // item is always 'assignment'
		itemid int **Optional** // when errorcode is 3 then itemid is an assignment id. When errorcode is 1, itemid is a course module id
		warningcode string // errorcode can be 3 (no user mappings found) or 1 (no permission to get user mappings)
		message string // untranslated english message to explain the warning
	}
]
```

<hr/>
</details>
<details>
<summary>mod_assign_list_participants</summary>
<br/>
<p>List the participants for a single assignment, with some summary info about their submissions.</p>
<h3>Parameters</h3>
```
assignid int // assign instance id
groupid int // group id
filter string // search string to filter the results
skip int // number of records to skip
limit int // maximum number of records to return
onlyids int // Do not return all user fields
includeenrolments int // Do return courses where the user is enrolled
tablesort int // Apply current user table sorting preferences.
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_lock_submissions</summary>
<br/>
<p>Prevent students from making changes to a list of submissions</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userids // 1 or more user ids
[
	{
		int // user id
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_reveal_identities</summary>
<br/>
<p>Reveal the identities for a blind marking assignment</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_revert_submissions_to_draft</summary>
<br/>
<p>Reverts the list of submissions to draft status</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userids // 1 or more user ids
[
	{
		int // user id
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_save_grade</summary>
<br/>
<p>Save a grade update for a single student.</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userid int // The student id to operate on
grade double // The new grade for this user. Ignored if advanced grading used
attemptnumber int // The attempt number (-1 means latest attempt)
addattempt int // Allow another attempt if the attempt reopen method is manual
workflowstate string // The next marking workflow state
applytoall int // If true, this grade will be applied to all members of the group (for group assignments).
plugindata // plugin data
{
	assignfeedbackcomments_editor **Optional** // Editor structure
	{
		text string // The text for this feedback.
		format int // The format for this feedback
	}
	files_filemanager int **Optional** // The id of a draft area containing files for this feedback.
}
advancedgradingdata // advanced grading data
{
	guide **Optional** // items
	{
		criteria // 
		[
			{
				criterionid int // criterion id
				fillings **Optional** // filling
				[
					{
						criterionid int // criterion id
						levelid int **Optional** // level id
						remark string **Optional** // remark
						remarkformat int **Optional** // remark format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
						score double // maximum score
					}
				]
			}
		]
	}
	rubric **Optional** // items
	{
		criteria // 
		[
			{
				criterionid int // criterion id
				fillings **Optional** // filling
				[
					{
						criterionid int // criterion id
						levelid int **Optional** // level id
						remark string **Optional** // remark
						remarkformat int **Optional** // remark format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					}
				]
			}
		]
	}
}
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_save_grades</summary>
<br/>
<p>Save multiple grade updates for an assignment.</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
applytoall int // If true, this grade will be applied to all members of the group (for group assignments).
grades // 
[
	{
		userid int // The student id to operate on
		grade double // The new grade for this user. Ignored if advanced grading used
		attemptnumber int // The attempt number (-1 means latest attempt)
		addattempt int // Allow another attempt if manual attempt reopen method
		workflowstate string // The next marking workflow state
		plugindata // plugin data
		{
			assignfeedbackcomments_editor **Optional** // Editor structure
			{
				text string // The text for this feedback.
				format int // The format for this feedback
			}
			files_filemanager int **Optional** // The id of a draft area containing files for this feedback.
		}
		advancedgradingdata // advanced grading data
		{
			guide **Optional** // items
			{
				criteria // 
				[
					{
						criterionid int // criterion id
						fillings **Optional** // filling
						[
							{
								criterionid int // criterion id
								levelid int **Optional** // level id
								remark string **Optional** // remark
								remarkformat int **Optional** // remark format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
								score double // maximum score
							}
						]
					}
				]
			}
			rubric **Optional** // items
			{
				criteria // 
				[
					{
						criterionid int // criterion id
						fillings **Optional** // filling
						[
							{
								criterionid int // criterion id
								levelid int **Optional** // level id
								remark string **Optional** // remark
								remarkformat int **Optional** // remark format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
							}
						]
					}
				]
			}
		}
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

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
<summary>mod_assign_save_user_extensions</summary>
<br/>
<p>Save a list of assignment extensions</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userids // 1 or more user ids
[
	{
		int // user id
	}
]
dates // 1 or more extension dates (timestamp)
[
	{
		int // dates
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_set_user_flags</summary>
<br/>
<p>Creates or updates user flags</p>
<h3>Parameters</h3>
```
assignmentid int // assignment id
userflags // 
[
	{
		userid int // student id
		locked int **Optional** // locked
		mailed int **Optional** // mailed
		extensionduedate int **Optional** // extension due date
		workflowstate string **Optional** // marking workflow state
		allocatedmarker int **Optional** // allocated marker
	}
]
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
<details>
<summary>mod_assign_submit_grading_form</summary>
<br/>
<p>Submit the grading form data via ajax</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userid int // The user id the submission belongs to
jsonformdata string // The data from the grading form, encoded as a json array
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_unlock_submissions</summary>
<br/>
<p>Allow students to make changes to a list of submissions</p>
<h3>Parameters</h3>
```
assignmentid int // The assignment id to operate on
userids // 1 or more user ids
[
	{
		int // user id
	}
]
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>mod_assign_view_assign</summary>
<br/>
<p>Update the module completion status.</p>
<h3>Parameters</h3>
```
assignid int // assign instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_assign_view_grading_table</summary>
<br/>
<p>Trigger the grading_table_viewed event.</p>
<h3>Parameters</h3>
```
assignid int // assign instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_assign_view_submission_status</summary>
<br/>
<p>Trigger the submission status viewed event.</p>
<h3>Parameters</h3>
```
assignid int // assign instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>mod_book_view_book</summary>
<br/>
<p>Simulate the view.php web interface book: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
bookid int // book instance id
chapterid int // chapter id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_chat_get_chats_by_courses</summary>
<br/>
<p>Returns a list of chat instances in a provided set of courses,
                            if no courses are provided then all the chat instances the user has access to will be returned.</p>
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
chats // 
[
	{
		id int // Chat id
		coursemodule int // Course module id
		course int // Course id
		name string // Chat name
		intro string // The Chat intro
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
		chatmethod string **Optional** // chat method (sockets, ajax, header_js)
		keepdays int **Optional** // keep days
		studentlogs int **Optional** // student logs visible to everyone
		chattime int **Optional** // chat time
		schedule int **Optional** // schedule type
		timemodified int **Optional** // time of last modification
		section int **Optional** // course section id
		visible int **Optional** // visible
		groupmode int **Optional** // group mode
		groupingid int **Optional** // group id
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
<summary>mod_chat_get_chat_latest_messages</summary>
<br/>
<p>Get the latest messages from the given chat session.</p>
<h3>Parameters</h3>
```
chatsid string // chat session id (obtained via mod_chat_login_user)
chatlasttime int // last time messages were retrieved (epoch time)
```

<h3>Returns</h3>
```
messages // list of users
[
	{
		id int // message id
		userid int // user id
		system int // true if is a system message (like user joined)
		message string // message text
		timestamp int // timestamp for the message
	}
]
chatnewlasttime int // new last time
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
<summary>mod_chat_get_chat_users</summary>
<br/>
<p>Get the list of users in the given chat session.</p>
<h3>Parameters</h3>
```
chatsid string // chat session id (obtained via mod_chat_login_user)
```

<h3>Returns</h3>
```
users // list of users
[
	{
		id int // user id
		fullname string // user full name
		profileimageurl string // user picture URL
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
<summary>mod_chat_get_sessions</summary>
<br/>
<p>Retrieves chat sessions for a given chat.</p>
<h3>Parameters</h3>
```
chatid int // Chat instance id.
groupid int // Get messages from users in this group.
                                                0 means that the function will determine the user group
showall int // Whether to show completed sessions or not.
```

<h3>Returns</h3>
```
sessions // list of users
[
	{
		sessionstart int // Session start time.
		sessionend int // Session end time.
		sessionusers // Session users.
		[
			{
				userid int // User id.
				messagecount int // Number of messages in the session.
			}
		]
		iscomplete int // Whether the session is completed or not.
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
<summary>mod_chat_get_session_messages</summary>
<br/>
<p>Retrieves messages of the given chat session.</p>
<h3>Parameters</h3>
```
chatid int // Chat instance id.
sessionstart int // The session start time (timestamp).
sessionend int // The session end time (timestamp).
groupid int // Get messages from users in this group.
                                                0 means that the function will determine the user group
```

<h3>Returns</h3>
```
messages // 
[
	{
		id int // The message record id.
		chatid int // The chat id.
		userid int // The user who wrote the message.
		groupid int // The group this message belongs to.
		issystem int // Whether is a system message or not.
		message string // The message text.
		timestamp int // The message timestamp (indicates when the message was sent).
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
<summary>mod_chat_login_user</summary>
<br/>
<p>Log a user into a chat room in the given chat.</p>
<h3>Parameters</h3>
```
chatid int // chat instance id
groupid int // group id, 0 means that the function will determine the user group
```

<h3>Returns</h3>
```
chatsid string // unique chat session id
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
<summary>mod_chat_send_chat_message</summary>
<br/>
<p>Send a message on the given chat session.</p>
<h3>Parameters</h3>
```
chatsid string // chat session id (obtained via mod_chat_login_user)
messagetext string // the message text
beepid string // the beep id
```

<h3>Returns</h3>
```
messageid int // message sent id
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
<summary>mod_chat_view_chat</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
chatid int // chat instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
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
<summary>mod_choice_get_choice_results</summary>
<br/>
<p>Retrieve users results for a given choice.</p>
<h3>Parameters</h3>
```
choiceid int // choice instance id
```

<h3>Returns</h3>
```
options // 
[
	{
		id int // choice instance id
		text string // text of the choice
		maxanswer int // maximum number of answers
		userresponses // 
		[
			{
				userid int // user id
				fullname string // user full name
				profileimageurl string // profile user image url
				answerid int **Optional** // answer id
				timemodified int **Optional** // time of modification
			}
		]
		numberofuser int // number of users answers
		percentageamount double // percentage of users answers
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
<details>
<summary>mod_choice_view_choice</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
choiceid int // choice instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_data_add_entry</summary>
<br/>
<p>Adds a new entry.</p>
<h3>Parameters</h3>
```
databaseid int // data instance id
groupid int // Group id, 0 means that the function will determine the user group
data // The fields data to be created
[
	{
		fieldid int // The field id.
		subfield string // The subfield name (if required).
		value string // The contents for the field always JSON encoded.
	}
]
```

<h3>Returns</h3>
```
newentryid int // True new created entry id. 0 if the entry was not created.
generalnotifications // 
[
	{
		string // General notifications
	}
]
fieldnotifications // 
[
	{
		fieldname string // The field name.
		notification string // The notification for the field.
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
<summary>mod_data_approve_entry</summary>
<br/>
<p>Approves or unapproves an entry.</p>
<h3>Parameters</h3>
```
entryid int // Record entry id.
approve int // Whether to approve (true) or unapprove the entry.
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_data_delete_entry</summary>
<br/>
<p>Deletes an entry.</p>
<h3>Parameters</h3>
```
entryid int // Record entry id.
```

<h3>Returns</h3>
```
status int // Always true. If we see this field it means that the entry was deleted.
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
<details>
<summary>mod_data_update_entry</summary>
<br/>
<p>Updates an existing entry.</p>
<h3>Parameters</h3>
```
entryid int // The entry record id.
data // The fields data to be updated
[
	{
		fieldid int // The field id.
		subfield string // The subfield name (if required).
		value string // The new contents for the field always JSON encoded.
	}
]
```

<h3>Returns</h3>
```
updated int // True if the entry was successfully updated, false other wise.
generalnotifications // 
[
	{
		string // General notifications
	}
]
fieldnotifications // 
[
	{
		fieldname string // The field name.
		notification string // The notification for the field.
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
<summary>mod_data_view_database</summary>
<br/>
<p>Simulate the view.php web interface data: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
databaseid int // data instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_feedback_get_analysis</summary>
<br/>
<p>Retrieves the feedback analysis.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
groupid int // Group id, 0 means that the function will determine the user group
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
completedcount int // Number of completed submissions.
itemscount int // Number of items (questions).
itemsdata // 
[
	{
		item // 
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
		data // 
		[
			{
		string // The analysis data (can be json encoded)
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
<summary>mod_feedback_get_current_completed_tmp</summary>
<br/>
<p>Returns the temporary completion record for the current user.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
feedback // 
{
	id int // The record id.
	feedback int // The feedback instance id this records belongs to.
	userid int // The user who completed the feedback (0 for anonymous).
	guestid string // For guests, this is the session key.
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
<summary>mod_feedback_get_non_respondents</summary>
<br/>
<p>Retrieves a list of students who didn't submit the feedback.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
groupid int // Group id, 0 means that the function will determine the user group.
sort string // Sort param, must be firstname, lastname or lastaccess (default).
page int // The page of records to return.
perpage int // The number of records to return per page.
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
users // 
[
	{
		courseid int // Course id
		userid int // The user id
		fullname string // User full name
		started int // If the user has started the attempt
	}
]
total int // Total number of non respondents
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
<details>
<summary>mod_feedback_get_responses_analysis</summary>
<br/>
<p>Return the feedback user responses analysis.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
groupid int // Group id, 0 means that the function will determine the user group
page int // The page of records to return.
perpage int // The number of records to return per page
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
attempts // 
[
	{
		id int // Completed id
		courseid int // Course id
		userid int // User who responded
		timemodified int // Time modified for the response
		fullname string // User full name
		responses // 
		[
			{
				id int // Response id
				name string // Response name
				printval string // Response ready for output
				rawval string // Response raw value
			}
		]
	}
]
totalattempts int // Total responses count.
anonattempts // 
[
	{
		id int // Completed id
		courseid int // Course id
		number int // Response number
		responses // 
		[
			{
				id int // Response id
				name string // Response name
				printval string // Response ready for output
				rawval string // Response raw value
			}
		]
	}
]
totalanonattempts int // Total anonymous responses count.
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
<summary>mod_feedback_get_unfinished_responses</summary>
<br/>
<p>Retrieves responses from the current unfinished attempt.</p>
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
		completed int // Reference to the feedback_completedtmp table.
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
<summary>mod_feedback_launch_feedback</summary>
<br/>
<p>Starts or continues a feedback submission.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
gopage int // The next page to go (-1 if we were already in the last page). 0 for first page.
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
<summary>mod_feedback_process_page</summary>
<br/>
<p>Process a jump between pages.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id.
page int // The page being processed.
responses // The data to be processed.
[
	{
		name string // The response name (usually type[index]_id).
		value string // The response value.
	}
]
goprevious int // Whether we want to jump to previous page.
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
jumpto int // The page to jump to.
completed int // If the user completed the feedback.
completionpagecontents string // The completion page contents.
siteaftersubmit string // The link (could be relative) to show after submit.
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
<summary>mod_feedback_view_feedback</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
feedbackid int // Feedback instance id
moduleviewed int // If we need to mark the module as viewed for completion
courseid int // Course where user completes the feedback (for site feedbacks only).
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>mod_folder_view_folder</summary>
<br/>
<p>Simulate the view.php web interface folder: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
folderid int // folder instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_forum_prepare_draft_area_for_post</summary>
<br/>
<p>Prepares a draft area for editing a post.</p>
<h3>Parameters</h3>
```
postid int // Post to prepare the draft area for.
area string // Area to prepare: attachment or post.
draftitemid int // The draft item id to use. 0 to generate one.
filestokeep // Only keep these files in the draft file area. Empty for keeping all.
[
	{
		filename string // File name.
		filepath string // File path.
	}
]
```

<h3>Returns</h3>
```
draftitemid int // Draft item id for the file area.
files **Optional** // Draft area files.
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
areaoptions // Draft file area options.
[
	{
		name string // Name of option.
		value string // Value of option.
	}
]
messagetext string // Message text with URLs rewritten.
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
<summary>mod_forum_set_lock_state</summary>
<br/>
<p>Set the lock state for the discussion</p>
<h3>Parameters</h3>
```
forumid int // Forum that the discussion is in
discussionid int // The discussion to lock / unlock
targetstate int // The timestamp for the lock state
```

<h3>Returns</h3>
```
id int // The discussion we are locking.
locked int // The locked state of the discussion.
times // 
{
	locked int // The locked time of the discussion.
}
```

<hr/>
</details>
<details>
<summary>mod_forum_set_pin_state</summary>
<br/>
<p>Set the pin state</p>
<h3>Parameters</h3>
```
discussionid int // The discussion to pin or unpin
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
<details>
<summary>mod_forum_update_discussion_post</summary>
<br/>
<p>Updates a post or a discussion topic post.</p>
<h3>Parameters</h3>
```
postid int // Post to be updated. It can be a discussion topic post.
subject string // Updated post subject
message string // Updated post message (HTML assumed if messageformat is not provided)
messageformat int // message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
options // Configuration options for the post.
[
	{
		name string // The allowed keys (value format) are:
                                pinned (bool); (only for discussions) whether to pin this discussion or not
                                discussionsubscribe (bool); whether to subscribe to the post or not
                                inlineattachmentsid (int); the draft file area id for inline attachments in the text
                                attachmentsid (int); the draft file area id for attachments
		value string // The value of the option.
	}
]
```

<h3>Returns</h3>
```
status int // True if the post/discussion was updated, false otherwise.
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
<summary>mod_forum_view_forum</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
forumid int // forum instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_forum_view_forum_discussion</summary>
<br/>
<p>Trigger the forum discussion viewed event.</p>
<h3>Parameters</h3>
```
discussionid int // discussion id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_glossary_add_entry</summary>
<br/>
<p>Add a new entry to a given glossary</p>
<h3>Parameters</h3>
```
glossaryid int // Glossary id
concept string // Glossary concept
definition string // Glossary concept definition
definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
options // Optional settings
[
	{
		name string // The allowed keys (value format) are:
                            inlineattachmentsid (int); the draft file area id for inline attachments
                            attachmentsid (int); the draft file area id for attachments
                            categories (comma separated int); comma separated category ids
                            aliases (comma separated str); comma separated aliases
                            usedynalink (bool); whether the entry should be automatically linked.
                            casesensitive (bool); whether the entry is case sensitive.
                            fullmatch (bool); whether to match whole words only.
		value string // the value of the option (validated inside the function)
	}
]
```

<h3>Returns</h3>
```
entryid int // New glossary entry ID
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
<summary>mod_glossary_delete_entry</summary>
<br/>
<p>Delete the given entry from the glossary.</p>
<h3>Parameters</h3>
```
entryid int // Glossary entry id to delete
```

<h3>Returns</h3>
```
result int // The processing result
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
<summary>mod_glossary_get_entries_to_approve</summary>
<br/>
<p>Browse entries to be approved.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
letter string // A letter, or either keywords: 'ALL' or 'SPECIAL'.
order string // Order by: 'CONCEPT', 'CREATION' or 'UPDATE'
sort string // The direction of the order: 'ASC' or 'DESC'
from int // Start returning records from here
limit int // Number of records to return
options <br />
<b>Notice</b>:  Undefined property: external_single_structure::$type in <b>/bitnami/moodle/local/wstemplate/docs.php</b> on line <b>65</b><br />
string // An array of options
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
<details>
<summary>mod_glossary_prepare_entry_for_edition</summary>
<br/>
<p>Prepares the given entry for edition returning draft item areas and file areas information.</p>
<h3>Parameters</h3>
```
entryid int // Glossary entry id to update
```

<h3>Returns</h3>
```
inlineattachmentsid int // Draft item id for the text editor.
attachmentsid int // Draft item id for the file manager.
areas // File areas including options
[
	{
		area string // File area name.
		options // Draft file area options.
		[
			{
				name string // Name of option.
				value string // Value of option.
			}
		]
	}
]
aliases // 
[
	{
		string // Alias name.
	}
]
categories // 
[
	{
		int // Category id
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
<summary>mod_glossary_update_entry</summary>
<br/>
<p>Updates the given glossary entry.</p>
<h3>Parameters</h3>
```
entryid int // Glossary entry id to update
concept string // Glossary concept
definition string // Glossary concept definition
definitionformat int // definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
options // Optional settings
[
	{
		name string // The allowed keys (value format) are:
                            inlineattachmentsid (int); the draft file area id for inline attachments
                            attachmentsid (int); the draft file area id for attachments
                            categories (comma separated int); comma separated category ids
                            aliases (comma separated str); comma separated aliases
                            usedynalink (bool); whether the entry should be automatically linked.
                            casesensitive (bool); whether the entry is case sensitive.
                            fullmatch (bool); whether to match whole words only.
		value string // the value of the option (validated inside the function)
	}
]
```

<h3>Returns</h3>
```
result int // The update result
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
<summary>mod_glossary_view_entry</summary>
<br/>
<p>Notify a glossary entry as being viewed.</p>
<h3>Parameters</h3>
```
id int // Glossary entry ID
```

<h3>Returns</h3>
```
status int // True on success
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
<summary>mod_glossary_view_glossary</summary>
<br/>
<p>Notify the glossary as being viewed.</p>
<h3>Parameters</h3>
```
id int // Glossary instance ID
mode string // The mode in which the glossary is viewed
```

<h3>Returns</h3>
```
status int // True on success
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
<summary>mod_h5pactivity_get_attempts</summary>
<br/>
<p>Return the information needed to list a user attempts.</p>
<h3>Parameters</h3>
```
h5pactivityid int // h5p activity instance id
userids // User ids
[
	{
		int // The user ids to get attempts (null means only current user)
	}
]
```

<h3>Returns</h3>
```
activityid int // Activity course module ID
usersattempts // The complete users attempts list
[
	{
		userid int // The user id
		attempts // The complete attempts list
		[
			{
				id int // ID of the context
				h5pactivityid int // ID of the H5P activity
				userid int // ID of the user
				timecreated int // Attempt creation
				timemodified int // Attempt modified
				attempt int // Attempt number
				rawscore int // Attempt score value
				maxscore int // Attempt max score
				duration int // Attempt duration in seconds
				completion int **Optional** // Attempt completion
				success int **Optional** // Attempt success
				scaled double // Attempt scaled
			}
		]
		scored **Optional** // Attempts used to grade the activity
		{
			title string // Scored attempts title
			grademethod string // Scored attempts title
			attempts // List of the grading attempts
			[
				{
					id int // ID of the context
					h5pactivityid int // ID of the H5P activity
					userid int // ID of the user
					timecreated int // Attempt creation
					timemodified int // Attempt modified
					attempt int // Attempt number
					rawscore int // Attempt score value
					maxscore int // Attempt max score
					duration int // Attempt duration in seconds
					completion int **Optional** // Attempt completion
					success int **Optional** // Attempt success
					scaled double // Attempt scaled
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
<summary>mod_h5pactivity_get_h5pactivities_by_courses</summary>
<br/>
<p>Returns a list of h5p activities in a list of
            provided courses, if no list is provided all h5p activities
            that the user can view will be returned.</p>
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
h5pactivities // 
[
	{
		id int // The primary key of the record.
		course int // Course id this h5p activity is part of.
		name string // The name of the activity module instance.
		timecreated int **Optional** // Timestamp of when the instance was added to the course.
		timemodified int **Optional** // Timestamp of when the instance was last modified.
		intro string // H5P activity description.
		introformat int // intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		grade int **Optional** // The maximum grade for submission.
		displayoptions int // H5P Button display options.
		enabletracking int // Enable xAPI tracking.
		grademethod int // Which H5P attempt is used for grading.
		contenthash string **Optional** // Sha1 hash of file content.
		coursemodule int // coursemodule
		context int // context
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
		package // package
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
		deployedfile **Optional** // 
		{
			filename string **Optional** // File name.
			filepath string **Optional** // File path.
			filesize int **Optional** // File size.
			fileurl string **Optional** // Downloadable file url.
			timemodified int **Optional** // Time modified.
			mimetype string **Optional** // File mime type.
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
<summary>mod_h5pactivity_get_h5pactivity_access_information</summary>
<br/>
<p>Return access information for a given h5p activity.</p>
<h3>Parameters</h3>
```
h5pactivityid int // h5p activity instance id
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
canview int **Optional** // Whether the user has the capability mod/h5pactivity:view allowed.
canaddinstance int **Optional** // Whether the user has the capability mod/h5pactivity:addinstance allowed.
cansubmit int **Optional** // Whether the user has the capability mod/h5pactivity:submit allowed.
canreviewattempts int **Optional** // Whether the user has the capability mod/h5pactivity:reviewattempts allowed.
```

<hr/>
</details>
<details>
<summary>mod_h5pactivity_get_results</summary>
<br/>
<p>Return the information needed to list a user attempt results.</p>
<h3>Parameters</h3>
```
h5pactivityid int // h5p activity instance id
attemptids // Attempt ids
[
	{
		int // The attempt id
	}
]
```

<h3>Returns</h3>
```
activityid int // Activity course module ID
attempts // The complete attempts list
[
	{
		id int // ID of the context
		h5pactivityid int // ID of the H5P activity
		userid int // ID of the user
		timecreated int // Attempt creation
		timemodified int // Attempt modified
		attempt int // Attempt number
		rawscore int // Attempt score value
		maxscore int // Attempt max score
		duration int // Attempt duration in seconds
		completion int **Optional** // Attempt completion
		success int **Optional** // Attempt success
		scaled double // Attempt scaled
		results **Optional** // The results of the attempt
		[
			{
				id int // ID of the context
				attemptid int // ID of the H5P attempt
				subcontent string // Subcontent identifier
				timecreated int // Result creation
				interactiontype string // Interaction type
				description string // Result description
				content string **Optional** // Result extra content
				rawscore int // Result score value
				maxscore int // Result max score
				duration int **Optional** // Result duration in seconds
				completion int **Optional** // Result completion
				success int **Optional** // Result success
				optionslabel string **Optional** // Label used for result options
				correctlabel string **Optional** // Label used for correct answers
				answerlabel string **Optional** // Label used for user answers
				track int **Optional** // If the result has valid track information
				options **Optional** // The statement options
				[
					{
						description string **Optional** // Option description
						id string **Optional** // Option string identifier
						correctanswer **Optional** // The option correct answer
						{
							answer string **Optional** // Option text value
							correct int **Optional** // If has to be displayed as correct
							incorrect int **Optional** // If has to be displayed as incorrect
							text int **Optional** // If has to be displayed as simple text
							checked int **Optional** // If has to be displayed as a checked option
							unchecked int **Optional** // If has to be displayed as a unchecked option
							pass int **Optional** // If has to be displayed as passed
							fail int **Optional** // If has to be displayed as failed
						}
						useranswer **Optional** // The option user answer
						{
							answer string **Optional** // Option text value
							correct int **Optional** // If has to be displayed as correct
							incorrect int **Optional** // If has to be displayed as incorrect
							text int **Optional** // If has to be displayed as simple text
							checked int **Optional** // If has to be displayed as a checked option
							unchecked int **Optional** // If has to be displayed as a unchecked option
							pass int **Optional** // If has to be displayed as passed
							fail int **Optional** // If has to be displayed as failed
						}
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
<summary>mod_h5pactivity_view_h5pactivity</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
h5pactivityid int // H5P activity instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_imscp_get_imscps_by_courses</summary>
<br/>
<p>Returns a list of IMSCP instances in a provided set of courses,
                            if no courses are provided then all the IMSCP instances the user has access to will be returned.</p>
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
imscps // 
[
	{
		id int // IMSCP id
		coursemodule int // Course module id
		course int // Course id
		name string // Activity name
		intro string **Optional** // The IMSCP intro
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
		revision int **Optional** // Revision
		keepold int **Optional** // Number of old IMSCP to keep
		structure string **Optional** // IMSCP structure
		timemodified string **Optional** // Time of last modification
		section int **Optional** // Course section id
		visible int **Optional** // If visible
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
<summary>mod_imscp_view_imscp</summary>
<br/>
<p>Simulate the view.php web interface imscp: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
imscpid int // imscp instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_label_get_labels_by_courses</summary>
<br/>
<p>Returns a list of labels in a provided list of courses, if no list is provided all labels that the user
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
labels // 
[
	{
		id int // Module id
		coursemodule int // Course module id
		course int // Course id
		name string // Label name
		intro string // Label contents
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
		timemodified int // Last time the label was modified
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
<details>
<summary>mod_lesson_finish_attempt</summary>
<br/>
<p>Finishes the current attempt.</p>
<h3>Parameters</h3>
```
lessonid int // Lesson instance id.
password string // Optional password (the lesson may be protected).
outoftime int // If the user run out of time.
review int // If we want to review just after finishing (1 hour margin).
```

<h3>Returns</h3>
```
data // The EOL page information data.
[
	{
		name string // Data name.
		value string // Data value.
		message string // Data message (translated string).
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
<summary>mod_lesson_get_attempts_overview</summary>
<br/>
<p>Get a list of all the attempts made by users in a lesson.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
groupid int // group id, 0 means that the function will determine the user group
```

<h3>Returns</h3>
```
data **Optional** // Attempts overview data (empty for no attemps).
{
	lessonscored int // True if the lesson was scored.
	numofattempts int // Number of attempts.
	avescore double // Average score.
	highscore double // High score.
	lowscore double // Low score.
	avetime int // Average time (spent in taking the lesson).
	hightime int // High time.
	lowtime int // Low time.
	students **Optional** // Students data, including attempts.
	[
		{
			id int // User id.
			fullname string // User full name.
			bestgrade double // Best grade.
			attempts // 
			[
				{
					try int // Attempt number.
					grade double // Attempt grade.
					timestart int // Attempt time started.
					timeend int // Attempt last time continued.
					end int // Attempt time ended.
				}
			]
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
<summary>mod_lesson_get_content_pages_viewed</summary>
<br/>
<p>Return the list of content pages viewed by a user during a lesson attempt.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
lessonattempt int // lesson attempt number
userid int // the user id (empty for current user)
```

<h3>Returns</h3>
```
pages // 
[
	{
		id int // The attempt id.
		lessonid int // The lesson id.
		pageid int // The page id.
		userid int // The user who viewed the page.
		retry int // The lesson attempt number.
		flag int // 1 if the next page was calculated randomly.
		timeseen int // The time the page was seen.
		nextpageid int // The next page chosen id.
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
<summary>mod_lesson_get_pages_possible_jumps</summary>
<br/>
<p>Return all the possible jumps for the pages in a given lesson.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
```

<h3>Returns</h3>
```
jumps // 
[
	{
		pageid int // The page id
		answerid int // The answer id
		jumpto int // The jump (page id or type of jump)
		calculatedjump int // The real page id (or EOL) to jump
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
<b>Notice</b>:  Undefined property: external_multiple_structure::$type in <b>/bitnami/moodle/local/wstemplate/docs.php</b> on line <b>65</b><br />
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
<details>
<summary>mod_lesson_get_user_timers</summary>
<br/>
<p>Return the timers in the current lesson for the given user.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
userid int // the user id (empty for current user)
```

<h3>Returns</h3>
```
timers // 
[
	{
		id int // The attempt id
		lessonid int // The lesson id
		userid int // The user id
		starttime int // First access time for a new timer session
		lessontime int // Last access time to the lesson during the timer session
		completed int // If the lesson for this timer was completed
		timemodifiedoffline int // Last modified time via webservices.
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
<summary>mod_lesson_launch_attempt</summary>
<br/>
<p>Starts a new attempt or continues an existing one.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
password string // optional password (the lesson may be protected)
pageid int // page id to continue from (only when continuing an attempt)
review int // if we want to review just after finishing
```

<h3>Returns</h3>
```
messages // 
[
	{
		message string // Message.
		type string // Message type: usually a CSS identifier like:
                                success, info, warning, error, notifyproblem, notifyerror, notifytiny, notifysuccess
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
<summary>mod_lesson_process_page</summary>
<br/>
<p>Processes page responses.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
pageid int // the page id
data // the data to be saved
[
	{
		name string // data name
		value string // data value
	}
]
password string // optional password (the lesson may be protected)
review int // if we want to review just after finishing (1 hour margin)
```

<h3>Returns</h3>
```
newpageid int // New page id (if a jump was made).
inmediatejump int // Whether the page processing redirect directly to anoter page.
nodefaultresponse int // Whether there is not a default response.
feedback string // The response feedback.
attemptsremaining int // Number of attempts remaining.
correctanswer int // Whether the answer is correct.
noanswer int // Whether there aren't answers.
isessayquestion int // Whether is a essay question.
maxattemptsreached int // Whether we reachered the max number of attempts.
response string // The response.
studentanswer string // The student answer.
userresponse string // The user response.
reviewmode int // Whether the user is reviewing.
ongoingscore string // The ongoing message.
progress int // Progress percentage in the lesson.
displaymenu int // Whether we should display the menu or not in this page.
messages // 
[
	{
		message string // Message.
		type string // Message type: usually a CSS identifier like:
                                success, info, warning, error, notifyproblem, notifyerror, notifytiny, notifysuccess
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
<summary>mod_lesson_view_lesson</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
lessonid int // lesson instance id
password string // lesson password
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_lti_get_ltis_by_courses</summary>
<br/>
<p>Returns a list of external tool instances in a provided set of courses, if
                            no courses are provided then all the external tool instances the user has access to will be returned.</p>
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
ltis // 
[
	{
		id int // External tool id
		coursemodule int // Course module id
		course int // Course id
		name string // LTI name
		intro string **Optional** // The LTI intro
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
		timecreated int **Optional** // Time of creation
		timemodified int **Optional** // Time of last modification
		typeid int **Optional** // Type id
		toolurl string **Optional** // Tool url
		securetoolurl string **Optional** // Secure tool url
		instructorchoicesendname string **Optional** // Instructor choice send name
		instructorchoicesendemailaddr int **Optional** // instructor choice send mail address
		instructorchoiceallowroster int **Optional** // Instructor choice allow roster
		instructorchoiceallowsetting int **Optional** // Instructor choice allow setting
		instructorcustomparameters string **Optional** // instructor custom parameters
		instructorchoiceacceptgrades int **Optional** // instructor choice accept grades
		grade int **Optional** // Enable grades
		launchcontainer int **Optional** // Launch container mode
		resourcekey string **Optional** // Resource key
		password string **Optional** // Shared secret
		debuglaunch int **Optional** // Debug launch
		showtitlelaunch int **Optional** // Show title launch
		showdescriptionlaunch int **Optional** // Show description launch
		servicesalt string **Optional** // Service salt
		icon string **Optional** // Alternative icon URL
		secureicon string **Optional** // Secure icon URL
		section int **Optional** // course section id
		visible int **Optional** // visible
		groupmode int **Optional** // group mode
		groupingid int **Optional** // group id
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
<summary>mod_lti_get_tool_launch_data</summary>
<br/>
<p>Return the launch data for a given external tool.</p>
<h3>Parameters</h3>
```
toolid int // external tool instance id
```

<h3>Returns</h3>
```
endpoint string // Endpoint URL
parameters // 
[
	{
		name string // Parameter name
		value string // Parameter value
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
<summary>mod_lti_view_lti</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
ltiid int // lti instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_offlinequiz_get_attempt_review</summary>
<br/>
<p>Get current user's review for the specified offlinequiz.</p>
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
grade string **Optional** // grade for the quiz (or empty or "notyetgraded")
maxgrade string **Optional** // maxgrade for the quiz 
rawgrade string **Optional** // grade for the quiz (or empty or "notyetgraded")
rawmaxgrade string **Optional** // grade for the quiz (or empty or "notyetgraded")
questions // question object
[
	{
		slot int // slot number
		type string // question type, i.e: multichoice
		sequencecheck int **Optional** // the number of real steps in this attempt
		lastactiontime int **Optional** // the timestamp of the most recent step in this question attempt
		hasautosavedstep int **Optional** // whether this question attempt has autosaved data
		state string **Optional** // the state where the question is in.
                    It will not be returned if the user cannot see it due to the quiz display correctness settings.
		status string **Optional** // current formatted state of the question
		mark string **Optional** // the mark awarded.
                    It will be returned only if the user is allowed to see it.
		maxmark double **Optional** // the maximum mark possible for this question attempt.
                    It will be returned only if the user is allowed to see it.
		settings string **Optional** // Question settings (JSON encoded).
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
<details>
<summary>mod_page_view_page</summary>
<br/>
<p>Simulate the view.php web interface page: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
pageid int // page instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
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
<summary>mod_quiz_get_attempt_data</summary>
<br/>
<p>Returns information for the given attempt page for a quiz attempt in progress.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
page int // page number
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
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
messages // access messages, will only be returned for users with mod/quiz:preview capability,
                    for other users this method will throw an exception if there are messages
[
	{
		string // access message
	}
]
nextpage int // next page number
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
<summary>mod_quiz_get_attempt_summary</summary>
<br/>
<p>Returns a summary of a quiz attempt before it is submitted.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
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
<summary>mod_quiz_get_quiz_feedback_for_grade</summary>
<br/>
<p>Get the feedback text that should be show to a student who got the given grade in the given quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
grade double // the grade to check
```

<h3>Returns</h3>
```
feedbacktext string // the comment that corresponds to this grade (empty for none)
feedbacktextformat int **Optional** // feedbacktext format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
feedbackinlinefiles **Optional** // feedback inline files
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
<details>
<summary>mod_quiz_process_attempt</summary>
<br/>
<p>Process responses during an attempt at a quiz and also deals with attempts finishing.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
data // the data to be saved
[
	{
		name string // data name
		value string // data value
	}
]
finishattempt int // whether to finish or not the attempt
timeup int // whether the WS was called by a timer when the time is up
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
state string // state: the new attempt state:
                                                                    inprogress, finished, overdue, abandoned
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
<summary>mod_quiz_save_attempt</summary>
<br/>
<p>Processes save requests during the quiz.
                            This function is intended for the quiz auto-save feature.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
data // the data to be saved
[
	{
		name string // data name
		value string // data value
	}
]
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_quiz_start_attempt</summary>
<br/>
<p>Starts a new attempt at a quiz.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
forcenew int // Whether to force a new attempt or not.
```

<h3>Returns</h3>
```
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
<summary>mod_quiz_view_attempt</summary>
<br/>
<p>Trigger the attempt viewed event.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
page int // page number
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_quiz_view_attempt_review</summary>
<br/>
<p>Trigger the attempt reviewed event.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_quiz_view_attempt_summary</summary>
<br/>
<p>Trigger the attempt summary viewed event.</p>
<h3>Parameters</h3>
```
attemptid int // attempt id
preflightdata // Preflight required data (like passwords)
[
	{
		name string // data name
		value string // data value
	}
]
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_quiz_view_quiz</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
quizid int // quiz instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>mod_resource_view_resource</summary>
<br/>
<p>Simulate the view.php web interface resource: trigger events, completion, etc...</p>
<h3>Parameters</h3>
```
resourceid int // resource instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_scorm_get_scorms_by_courses</summary>
<br/>
<p>Returns a list of scorm instances in a provided set of courses, if
                            no courses are provided then all the scorm instances the user has access to will be returned.</p>
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
scorms // 
[
	{
		id int // SCORM id
		coursemodule int // Course module id
		course int // Course id
		name string // SCORM name
		intro string // The SCORM intro
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
		packagesize int **Optional** // SCORM zip package size
		packageurl string **Optional** // SCORM zip package URL
		version string **Optional** // SCORM version (SCORM_12, SCORM_13, SCORM_AICC)
		maxgrade int **Optional** // Max grade
		grademethod int **Optional** // Grade method
		whatgrade int **Optional** // What grade
		maxattempt int **Optional** // Maximum number of attemtps
		forcecompleted int **Optional** // Status current attempt is forced to "completed"
		forcenewattempt int **Optional** // Controls re-entry behaviour
		lastattemptlock int **Optional** // Prevents to launch new attempts once finished
		displayattemptstatus int **Optional** // How to display attempt status
		displaycoursestructure int **Optional** // Display contents structure
		sha1hash string **Optional** // Package content or ext path hash
		md5hash string **Optional** // MD5 Hash of package file
		revision int **Optional** // Revison number
		launch int **Optional** // First content to launch
		skipview int **Optional** // How to skip the content structure page
		hidebrowse int **Optional** // Disable preview mode?
		hidetoc int **Optional** // How to display the SCORM structure in player
		nav int **Optional** // Show navigation buttons
		navpositionleft int **Optional** // Navigation position left
		navpositiontop int **Optional** // Navigation position top
		auto int **Optional** // Auto continue?
		popup int **Optional** // Display in current or new window
		width int **Optional** // Frame width
		height int **Optional** // Frame height
		timeopen int **Optional** // Available from
		timeclose int **Optional** // Available to
		displayactivityname int **Optional** // Display the activity name above the player?
		scormtype string **Optional** // SCORM type
		reference string **Optional** // Reference to the package
		protectpackagedownloads int **Optional** // Protect package downloads?
		updatefreq int **Optional** // Auto-update frequency for remote packages
		options string **Optional** // Additional options
		completionstatusrequired int **Optional** // Status passed/completed required?
		completionscorerequired int **Optional** // Minimum score required
		completionstatusallscos int **Optional** // Require all scos to return completion status
		autocommit int **Optional** // Save track data automatically?
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
<details>
<summary>mod_scorm_get_scorm_access_information</summary>
<br/>
<p>Return capabilities information for a given scorm.</p>
<h3>Parameters</h3>
```
scormid int // scorm instance id.
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
canaddinstance int **Optional** // Whether the user has the capability mod/scorm:addinstance allowed.
canviewreport int **Optional** // Whether the user has the capability mod/scorm:viewreport allowed.
canskipview int **Optional** // Whether the user has the capability mod/scorm:skipview allowed.
cansavetrack int **Optional** // Whether the user has the capability mod/scorm:savetrack allowed.
canviewscores int **Optional** // Whether the user has the capability mod/scorm:viewscores allowed.
candeleteresponses int **Optional** // Whether the user has the capability mod/scorm:deleteresponses allowed.
candeleteownresponses int **Optional** // Whether the user has the capability mod/scorm:deleteownresponses allowed.
```

<hr/>
</details>
<details>
<summary>mod_scorm_get_scorm_attempt_count</summary>
<br/>
<p>Return the number of attempts done by a user in the given SCORM.</p>
<h3>Parameters</h3>
```
scormid int // SCORM instance id
userid int // User id
ignoremissingcompletion int // Ignores attempts that haven't reported a grade/completion
```

<h3>Returns</h3>
```
attemptscount int // Attempts count
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
<summary>mod_scorm_get_scorm_scoes</summary>
<br/>
<p>Returns a list containing all the scoes data related to the given scorm id</p>
<h3>Parameters</h3>
```
scormid int // scorm instance id
organization string // organization id
```

<h3>Returns</h3>
```
scoes // 
[
	{
		id int // sco id
		scorm int // scorm id
		manifest string // manifest id
		organization string // organization id
		parent string // parent
		identifier string // identifier
		launch string // launch file
		scormtype string // scorm type (asset, sco)
		title string // sco title
		sortorder int // sort order
		extradata **Optional** // Additional SCO data
		[
			{
				element string // element name
				value string // element value
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
<summary>mod_scorm_get_scorm_sco_tracks</summary>
<br/>
<p>Retrieves SCO tracking data for the given user id and attempt number</p>
<h3>Parameters</h3>
```
scoid int // sco id
userid int // user id
attempt int // attempt number (0 for last attempt)
```

<h3>Returns</h3>
```
data // SCO data
{
	attempt int // Attempt number
	tracks // 
	[
		{
			element string // Element name
			value string // Element value
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
<summary>mod_scorm_get_scorm_user_data</summary>
<br/>
<p>Retrieves user tracking and SCO data and default SCORM values</p>
<h3>Parameters</h3>
```
scormid int // scorm instance id
attempt int // attempt number
```

<h3>Returns</h3>
```
data // 
[
	{
		scoid int // sco id
		userdata // 
		[
			{
				element string // element name
				value string // element value
			}
		]
		defaultdata // 
		[
			{
				element string // element name
				value string // element value
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
<summary>mod_scorm_insert_scorm_tracks</summary>
<br/>
<p>Saves a scorm tracking record.
                          It will overwrite any existing tracking data for this attempt.
                          Validation should be performed before running the function to ensure the user will not lose any existing
                          attempt data.</p>
<h3>Parameters</h3>
```
scoid int // SCO id
attempt int // attempt number
tracks // 
[
	{
		element string // element name
		value string // element value
	}
]
```

<h3>Returns</h3>
```
trackids // 
[
	{
		int // track id
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
<summary>mod_scorm_launch_sco</summary>
<br/>
<p>Trigger the SCO launched event.</p>
<h3>Parameters</h3>
```
scormid int // SCORM instance id
scoid int // SCO id (empty for launching the first SCO)
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_scorm_view_scorm</summary>
<br/>
<p>Trigger the course module viewed event.</p>
<h3>Parameters</h3>
```
scormid int // scorm instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>mod_survey_submit_answers</summary>
<br/>
<p>Submit the answers for a given survey.</p>
<h3>Parameters</h3>
```
surveyid int // Survey id
answers // 
[
	{
		key string // Answer key
		value string // Answer value
	}
]
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_survey_view_survey</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
surveyid int // survey instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<details>
<summary>mod_url_view_url</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
urlid int // url instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_wiki_edit_page</summary>
<br/>
<p>Save the contents of a page.</p>
<h3>Parameters</h3>
```
pageid int // Page ID.
content string // Page contents.
section string // Section page title.
```

<h3>Returns</h3>
```
pageid int // Edited page id.
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
<summary>mod_wiki_get_page_for_editing</summary>
<br/>
<p>Locks and retrieves info of page-section to be edited.</p>
<h3>Parameters</h3>
```
pageid int // Page ID to edit.
section string // Section page title.
lockonly int // Just renew lock and not return content.
```

<h3>Returns</h3>
```
pagesection // 
{
	content string **Optional** // The contents of the page-section to be edited.
	contentformat string **Optional** // Format of the original content of the page.
	version int // Latest version of the page.
	warnings **Optional** // list of warnings
	[
		{
			item string **Optional** // item
			itemid int **Optional** // item id
			warningcode string // the warning code can be used by the client app to implement specific behaviour
			message string // untranslated english message to explain the warning
		}
	]
}
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
<details>
<summary>mod_wiki_new_page</summary>
<br/>
<p>Create a new page in a subwiki.</p>
<h3>Parameters</h3>
```
title string // New page title.
content string // Page contents.
contentformat string // Page contents format. If an invalid format is provided, default
                    wiki format is used.
subwikiid int // Page's subwiki ID.
wikiid int // Page's wiki ID. Used if subwiki does not exists.
userid int // Subwiki's user ID. Used if subwiki does not exists.
groupid int // Subwiki's group ID. Used if subwiki does not exists.
```

<h3>Returns</h3>
```
pageid int // New page id.
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
<summary>mod_wiki_view_page</summary>
<br/>
<p>Trigger the page viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
pageid int // Wiki page ID.
```

<h3>Returns</h3>
```
status int // Status: true if success.
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
<summary>mod_wiki_view_wiki</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
wikiid int // Wiki instance ID.
```

<h3>Returns</h3>
```
status int // Status: true if success.
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
<summary>mod_workshop_add_submission</summary>
<br/>
<p>Add a new submission to a given workshop.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop id
title string // Submission title
content string // Submission text content
contentformat int // The format used for the content
inlineattachmentsid int // The draft file area id for inline attachments in the content
attachmentsid int // The draft file area id for attachments
```

<h3>Returns</h3>
```
status int // True if the submission was created false otherwise.
submissionid int **Optional** // New workshop submission id.
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
<summary>mod_workshop_delete_submission</summary>
<br/>
<p>Deletes the given submission.</p>
<h3>Parameters</h3>
```
submissionid int // Submission id
```

<h3>Returns</h3>
```
status int // True if the submission was deleted.
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
<summary>mod_workshop_evaluate_assessment</summary>
<br/>
<p>Evaluates an assessment (used by teachers for provide feedback to the reviewer).</p>
<h3>Parameters</h3>
```
assessmentid int // Assessment id.
feedbacktext string // The feedback for the reviewer.
feedbackformat int // The feedback format for text.
weight int // The new weight for the assessment.
gradinggradeover string // The new grading grade.
```

<h3>Returns</h3>
```
status int // status: true if the assessment was evaluated, false otherwise.
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
<summary>mod_workshop_evaluate_submission</summary>
<br/>
<p>Evaluates a submission (used by teachers for provide feedback or override the submission grade).</p>
<h3>Parameters</h3>
```
submissionid int // submission id.
feedbacktext string // The feedback for the author.
feedbackformat int // The feedback format for text.
published int // Publish the submission for others?.
gradeover string // The new submission grade.
```

<h3>Returns</h3>
```
status int // status: true if the submission was evaluated, false otherwise.
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
<summary>mod_workshop_get_assessment_form_definition</summary>
<br/>
<p>Retrieves the assessment form definition.</p>
<h3>Parameters</h3>
```
assessmentid int // Assessment id
mode string // The form mode (assessment or preview)
```

<h3>Returns</h3>
```
dimenssionscount int // The number of dimenssions used by the form.
descriptionfiles // Files in the description text
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
options // The form options.
[
	{
		name string // Option name.
		value string // Option value.
	}
]
fields // The form fields.
[
	{
		name string // Field name.
		value string // Field default value.
	}
]
current // The current field values.
[
	{
		name string // Field name.
		value string // Current field value.
	}
]
dimensionsinfo // The dimensions general information.
[
	{
		id int // Dimension id.
		min double // Minimum grade for the dimension.
		max double // Maximum grade for the dimension.
		weight string // The weight of the dimension.
		scale string **Optional** // Scale items (if used).
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
<summary>mod_workshop_get_grades_report</summary>
<br/>
<p>Retrieves the assessment grades report.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id.
groupid int // Group id, 0 means that the function will determine the user group.
sortby string // sort by this element: lastname, firstname, submissiontitle,
                    submissionmodified, submissiongrade, gradinggrade.
sortdirection string // sort direction: ASC or DESC
page int // The page of records to return.
perpage int // The number of records to return per page.
```

<h3>Returns</h3>
```
report // 
{
	grades // 
	[
		{
			userid int // The id of the user being displayed in the report.
			submissionid int // Submission id.
			submissiontitle string // Submission title.
			submissionmodified int // Timestamp submission was updated.
			submissiongrade double **Optional** // Aggregated grade for the submission.
			gradinggrade double **Optional** // Computed grade for the assessment.
			submissiongradeover double **Optional** // Grade for the assessment overrided
                                        by the teacher.
			submissiongradeoverby int **Optional** // The id of the user who overrided
                                        the grade.
			submissionpublished int **Optional** // Whether is a submission published.
			reviewedby **Optional** // The users who reviewed the
                                        user submission.
			[
				{
					userid int // The id of the user (0 when is configured to do not display names).
					assessmentid int // The id of the assessment.
					submissionid int // The id of the submission assessed.
					grade double // The grade for submission.
					gradinggrade double // The grade for assessment.
					gradinggradeover double // The aggregated grade overrided.
					weight int // The weight of the assessment for aggregation.
				}
			]
			reviewerof **Optional** // The assessments the user
                                        reviewed.
			[
				{
					userid int // The id of the user (0 when is configured to do not display names).
					assessmentid int // The id of the assessment.
					submissionid int // The id of the submission assessed.
					grade double // The grade for submission.
					gradinggrade double // The grade for assessment.
					gradinggradeover double // The aggregated grade overrided.
					weight int // The weight of the assessment for aggregation.
				}
			]
		}
	]
	totalcount int // Number of total submissions.
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
<details>
<summary>mod_workshop_update_assessment</summary>
<br/>
<p>Add information to an allocated assessment.</p>
<h3>Parameters</h3>
```
assessmentid int // Assessment id.
data // Assessment data
[
	{
		name string // The assessment data (use WS get_assessment_form_definition for obtaining the data to sent).
                                Apart from that data, you can optionally send:
                                feedbackauthor (str); the feedback for the submission author
                                feedbackauthorformat (int); the format of the feedbackauthor
                                feedbackauthorinlineattachmentsid (int); the draft file area for the editor attachments
                                feedbackauthorattachmentsid (int); the draft file area id for the feedback attachments
		value string // The value of the option.
	}
]
```

<h3>Returns</h3>
```
status int // status: true if the assessment was added or updated false otherwise.
rawgrade double **Optional** // Raw percentual grade (0.00000 to 100.00000) for submission.
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
<summary>mod_workshop_update_submission</summary>
<br/>
<p>Update the given submission.</p>
<h3>Parameters</h3>
```
submissionid int // Submission id
title string // Submission title
content string // Submission text content
contentformat int // The format used for the content
inlineattachmentsid int // The draft file area id for inline attachments in the content
attachmentsid int // The draft file area id for attachments
```

<h3>Returns</h3>
```
status int // True if the submission was updated false otherwise.
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
<summary>mod_workshop_view_submission</summary>
<br/>
<p>Trigger the submission viewed event.</p>
<h3>Parameters</h3>
```
submissionid int // Submission id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>mod_workshop_view_workshop</summary>
<br/>
<p>Trigger the course module viewed event and update the module completion status.</p>
<h3>Parameters</h3>
```
workshopid int // Workshop instance id
```

<h3>Returns</h3>
```
status int // status: true if success
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
<summary>report_insights_action_executed</summary>
<br/>
<p>Stores an action executed over a group of predictions.</p>
<h3>Parameters</h3>
```
actionname string // The name of the action
predictionids // Array of prediction ids
[
	{
		int // Prediction id
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
<details>
<summary>report_insights_set_fixed_prediction</summary>
<br/>
<p>Flags a prediction as fixed.</p>
<h3>Parameters</h3>
```
predictionid int // The prediction id
```

<h3>Returns</h3>
```
success int // True if the prediction was successfully flagged as fixed.
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
<summary>report_insights_set_notuseful_prediction</summary>
<br/>
<p>Flags the prediction as not useful.</p>
<h3>Parameters</h3>
```
predictionid int // The prediction id
```

<h3>Returns</h3>
```
success int // True if the prediction was successfully flagged as not useful.
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
<summary>tool_analytics_potential_contexts</summary>
<br/>
<p>Retrieve the list of potential contexts for a model.</p>
<h3>Parameters</h3>
```
query string // The model id
modelid int // The model id
```

<h3>Returns</h3>
<strong>No Return.</strong><br/>

<hr/>
</details>
<details>
<summary>tool_lp_data_for_course_competencies_page</summary>
<br/>
<p>Load the data for the course competencies page template.</p>
<h3>Parameters</h3>
```
courseid int // The course id
moduleid int // The module id
```

<h3>Returns</h3>
```
courseid int // The current course id
pagecontextid int // The current page context ID.
gradableuserid int **Optional** // Current user id, if the user is a gradable user.
canmanagecompetencyframeworks int // User can manage competency frameworks
canmanagecoursecompetencies int // User can manage linked course competencies
canconfigurecoursecompetencies int // User can configure course competency settings
cangradecompetencies int // User can grade competencies.
settings // 
{
	courseid int // courseid
	pushratingstouserplans int // pushratingstouserplans
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
}
statistics // 
{
	competencycount int // competencycount
	proficientcompetencycount int // proficientcompetencycount
	proficientcompetencypercentage double // proficientcompetencypercentage
	proficientcompetencypercentageformatted string // proficientcompetencypercentageformatted
	leastproficient // leastproficient
	[
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
	]
	leastproficientcount int // leastproficientcount
	canbegradedincourse int // canbegradedincourse
	canmanagecoursecompetencies int // canmanagecoursecompetencies
}
competencies // 
[
	{
		competency // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
		coursecompetency // 
		{
			courseid int // courseid
			competencyid int // competencyid
			sortorder int // sortorder
			ruleoutcome int // ruleoutcome
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
		coursemodules // 
		[
			{
				id int // id
				name string // name
				url string **Optional** // url
				iconurl string // iconurl
			}
		]
		usercompetencycourse **Optional** // 
		{
			userid int // userid
			courseid int // courseid
			competencyid int // competencyid
			proficiency int // proficiency
			grade int // grade
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			gradename string // gradename
			proficiencyname string // proficiencyname
		}
		ruleoutcomeoptions // 
		[
			{
				value int // The option value
				text string // The name of the option
				selected int // If this is the currently selected option
			}
		]
		comppath // 
		{
			ancestors // ancestors
			[
				{
					id int // id
					name string // name
					first int // first
					last int // last
					position int // position
				}
			]
			framework // 
			{
				id int // id
				name string // name
				first int // first
				last int // last
				position int // position
			}
			pluginbaseurl string // pluginbaseurl
			pagecontextid int // pagecontextid
			showlinks int // showlinks
		}
		plans // 
		[
			{
				name string // name
				description string // description
				descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				userid int // userid
				templateid int // templateid
				origtemplateid int // origtemplateid
				status int // status
				duedate int // duedate
				reviewerid int // reviewerid
				id int // id
				timecreated int // timecreated
				timemodified int // timemodified
				usermodified int // usermodified
				statusname string // statusname
				isbasedontemplate int // isbasedontemplate
				canmanage int // canmanage
				canrequestreview int // canrequestreview
				canreview int // canreview
				canbeedited int // canbeedited
				isactive int // isactive
				isdraft int // isdraft
				iscompleted int // iscompleted
				isinreview int // isinreview
				iswaitingforreview int // iswaitingforreview
				isreopenallowed int // isreopenallowed
				iscompleteallowed int // iscompleteallowed
				isunlinkallowed int // isunlinkallowed
				isrequestreviewallowed int // isrequestreviewallowed
				iscancelreviewrequestallowed int // iscancelreviewrequestallowed
				isstartreviewallowed int // isstartreviewallowed
				isstopreviewallowed int // isstopreviewallowed
				isapproveallowed int // isapproveallowed
				isunapproveallowed int // isunapproveallowed
				duedateformatted string // duedateformatted
				commentarea // 
				{
					component string // component
					commentarea string // commentarea
					itemid int // itemid
					courseid int // courseid
					contextid int // contextid
					cid string // cid
					autostart int // autostart
					canpost int // canpost
					canview int // canview
					count int // count
					collapsediconkey string // collapsediconkey
					displaytotalcount int // displaytotalcount
					displaycancel int // displaycancel
					fullwidth int // fullwidth
					linktext string // linktext
					notoggle int // notoggle
					template string // template
					canpostorhascomments int // canpostorhascomments
				}
				reviewer **Optional** // 
				{
					id int // id
					email string // email
					idnumber string // idnumber
					phone1 string // phone1
					phone2 string // phone2
					department string // department
					institution string // institution
					fullname string // fullname
					identity string // identity
					profileurl string // profileurl
					profileimageurl string // profileimageurl
					profileimageurlsmall string // profileimageurlsmall
				}
				template **Optional** // 
				{
					shortname string // shortname
					description string // description
					descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					duedate int // duedate
					visible int // visible
					contextid int // contextid
					id int // id
					timecreated int // timecreated
					timemodified int // timemodified
					usermodified int // usermodified
					duedateformatted string // duedateformatted
					cohortscount int // cohortscount
					planscount int // planscount
					canmanage int // canmanage
					canread int // canread
					contextname string // contextname
					contextnamenoprefix string // contextnamenoprefix
				}
				url string // url
			}
		]
	}
]
manageurl string // Url to the manage competencies page.
pluginbaseurl string // Url to the course competencies page.
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_plans_page</summary>
<br/>
<p>Load the data for the plans page template</p>
<h3>Parameters</h3>
```
userid int // The user id
```

<h3>Returns</h3>
```
userid int // The learning plan user id
plans // 
[
	{
		name string // name
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		userid int // userid
		templateid int // templateid
		origtemplateid int // origtemplateid
		status int // status
		duedate int // duedate
		reviewerid int // reviewerid
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		statusname string // statusname
		isbasedontemplate int // isbasedontemplate
		canmanage int // canmanage
		canrequestreview int // canrequestreview
		canreview int // canreview
		canbeedited int // canbeedited
		isactive int // isactive
		isdraft int // isdraft
		iscompleted int // iscompleted
		isinreview int // isinreview
		iswaitingforreview int // iswaitingforreview
		isreopenallowed int // isreopenallowed
		iscompleteallowed int // iscompleteallowed
		isunlinkallowed int // isunlinkallowed
		isrequestreviewallowed int // isrequestreviewallowed
		iscancelreviewrequestallowed int // iscancelreviewrequestallowed
		isstartreviewallowed int // isstartreviewallowed
		isstopreviewallowed int // isstopreviewallowed
		isapproveallowed int // isapproveallowed
		isunapproveallowed int // isunapproveallowed
		duedateformatted string // duedateformatted
		commentarea // 
		{
			component string // component
			commentarea string // commentarea
			itemid int // itemid
			courseid int // courseid
			contextid int // contextid
			cid string // cid
			autostart int // autostart
			canpost int // canpost
			canview int // canview
			count int // count
			collapsediconkey string // collapsediconkey
			displaytotalcount int // displaytotalcount
			displaycancel int // displaycancel
			fullwidth int // fullwidth
			linktext string // linktext
			notoggle int // notoggle
			template string // template
			canpostorhascomments int // canpostorhascomments
		}
		reviewer **Optional** // 
		{
			id int // id
			email string // email
			idnumber string // idnumber
			phone1 string // phone1
			phone2 string // phone2
			department string // department
			institution string // institution
			fullname string // fullname
			identity string // identity
			profileurl string // profileurl
			profileimageurl string // profileimageurl
			profileimageurlsmall string // profileimageurlsmall
		}
		template **Optional** // 
		{
			shortname string // shortname
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			duedate int // duedate
			visible int // visible
			contextid int // contextid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			duedateformatted string // duedateformatted
			cohortscount int // cohortscount
			planscount int // planscount
			canmanage int // canmanage
			canread int // canread
			contextname string // contextname
			contextnamenoprefix string // contextnamenoprefix
		}
		url string // url
	}
]
pluginbaseurl string // Url to the tool_lp plugin folder on this Moodle site
navigation // 
[
	{
		string // HTML for a navigation item that should be on this page
	}
]
canreaduserevidence int // Can the current user view the user's evidence
canmanageuserplans int // Can the current user manage the user's plans
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_plan_page</summary>
<br/>
<p>Load the data for the plan page template.</p>
<h3>Parameters</h3>
```
planid int // The plan id
```

<h3>Returns</h3>
```
plan // 
{
	name string // name
	description string // description
	descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	userid int // userid
	templateid int // templateid
	origtemplateid int // origtemplateid
	status int // status
	duedate int // duedate
	reviewerid int // reviewerid
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	statusname string // statusname
	isbasedontemplate int // isbasedontemplate
	canmanage int // canmanage
	canrequestreview int // canrequestreview
	canreview int // canreview
	canbeedited int // canbeedited
	isactive int // isactive
	isdraft int // isdraft
	iscompleted int // iscompleted
	isinreview int // isinreview
	iswaitingforreview int // iswaitingforreview
	isreopenallowed int // isreopenallowed
	iscompleteallowed int // iscompleteallowed
	isunlinkallowed int // isunlinkallowed
	isrequestreviewallowed int // isrequestreviewallowed
	iscancelreviewrequestallowed int // iscancelreviewrequestallowed
	isstartreviewallowed int // isstartreviewallowed
	isstopreviewallowed int // isstopreviewallowed
	isapproveallowed int // isapproveallowed
	isunapproveallowed int // isunapproveallowed
	duedateformatted string // duedateformatted
	commentarea // 
	{
		component string // component
		commentarea string // commentarea
		itemid int // itemid
		courseid int // courseid
		contextid int // contextid
		cid string // cid
		autostart int // autostart
		canpost int // canpost
		canview int // canview
		count int // count
		collapsediconkey string // collapsediconkey
		displaytotalcount int // displaytotalcount
		displaycancel int // displaycancel
		fullwidth int // fullwidth
		linktext string // linktext
		notoggle int // notoggle
		template string // template
		canpostorhascomments int // canpostorhascomments
	}
	reviewer **Optional** // 
	{
		id int // id
		email string // email
		idnumber string // idnumber
		phone1 string // phone1
		phone2 string // phone2
		department string // department
		institution string // institution
		fullname string // fullname
		identity string // identity
		profileurl string // profileurl
		profileimageurl string // profileimageurl
		profileimageurlsmall string // profileimageurlsmall
	}
	template **Optional** // 
	{
		shortname string // shortname
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		duedate int // duedate
		visible int // visible
		contextid int // contextid
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		duedateformatted string // duedateformatted
		cohortscount int // cohortscount
		planscount int // planscount
		canmanage int // canmanage
		canread int // canread
		contextname string // contextname
		contextnamenoprefix string // contextnamenoprefix
	}
	url string // url
}
contextid int // Context ID.
pluginbaseurl string // Plugin base URL.
competencies // 
[
	{
		competency // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
		comppath // 
		{
			ancestors // ancestors
			[
				{
					id int // id
					name string // name
					first int // first
					last int // last
					position int // position
				}
			]
			framework // 
			{
				id int // id
				name string // name
				first int // first
				last int // last
				position int // position
			}
			pluginbaseurl string // pluginbaseurl
			pagecontextid int // pagecontextid
			showlinks int // showlinks
		}
		usercompetency **Optional** // 
		{
			userid int // userid
			competencyid int // competencyid
			status int // status
			reviewerid int // reviewerid
			proficiency int // proficiency
			grade int // grade
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			canrequestreview int // canrequestreview
			canreview int // canreview
			gradename string // gradename
			isrequestreviewallowed int // isrequestreviewallowed
			iscancelreviewrequestallowed int // iscancelreviewrequestallowed
			isstartreviewallowed int // isstartreviewallowed
			isstopreviewallowed int // isstopreviewallowed
			isstatusidle int // isstatusidle
			isstatusinreview int // isstatusinreview
			isstatuswaitingforreview int // isstatuswaitingforreview
			proficiencyname string // proficiencyname
			reviewer **Optional** // 
			{
				id int // id
				email string // email
				idnumber string // idnumber
				phone1 string // phone1
				phone2 string // phone2
				department string // department
				institution string // institution
				fullname string // fullname
				identity string // identity
				profileurl string // profileurl
				profileimageurl string // profileimageurl
				profileimageurlsmall string // profileimageurlsmall
			}
			statusname string // statusname
			url string // url
		}
		usercompetencyplan **Optional** // 
		{
			userid int // userid
			competencyid int // competencyid
			proficiency int // proficiency
			grade int // grade
			planid int // planid
			sortorder int // sortorder
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			gradename string // gradename
			proficiencyname string // proficiencyname
		}
	}
]
competencycount int // Count of competencies
proficientcompetencycount int // Count of proficientcompetencies
proficientcompetencypercentage double // Percentage of competencies proficient
proficientcompetencypercentageformatted string // Displayable percentage
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_user_competency_summary</summary>
<br/>
<p>Load a summary of a user competency.</p>
<h3>Parameters</h3>
```
userid int // Data base record id for the user
competencyid int // Data base record id for the competency
```

<h3>Returns</h3>
```
showrelatedcompetencies int // showrelatedcompetencies
cangrade int // cangrade
competency // 
{
	linkedcourses // linkedcourses
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
	relatedcompetencies // relatedcompetencies
	[
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
	]
	competency // 
	{
		shortname string // shortname
		idnumber string // idnumber
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		sortorder int // sortorder
		parentid int // parentid
		path string // path
		ruleoutcome int // ruleoutcome
		ruletype string // ruletype
		ruleconfig string // ruleconfig
		scaleid int // scaleid
		scaleconfiguration string // scaleconfiguration
		competencyframeworkid int // competencyframeworkid
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
	}
	framework // 
	{
		shortname string // shortname
		idnumber string // idnumber
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		visible int // visible
		scaleid int // scaleid
		scaleconfiguration string // scaleconfiguration
		contextid int // contextid
		taxonomies string // taxonomies
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		canmanage int // canmanage
		competenciescount int // competenciescount
		contextname string // contextname
		contextnamenoprefix string // contextnamenoprefix
	}
	hascourses int // hascourses
	hasrelatedcompetencies int // hasrelatedcompetencies
	scaleid int // scaleid
	scaleconfiguration string // scaleconfiguration
	taxonomyterm string // taxonomyterm
	comppath // 
	{
		ancestors // ancestors
		[
			{
				id int // id
				name string // name
				first int // first
				last int // last
				position int // position
			}
		]
		framework // 
		{
			id int // id
			name string // name
			first int // first
			last int // last
			position int // position
		}
		pluginbaseurl string // pluginbaseurl
		pagecontextid int // pagecontextid
		showlinks int // showlinks
	}
	pluginbaseurl string // pluginbaseurl
}
user // 
{
	id int // id
	email string // email
	idnumber string // idnumber
	phone1 string // phone1
	phone2 string // phone2
	department string // department
	institution string // institution
	fullname string // fullname
	identity string // identity
	profileurl string // profileurl
	profileimageurl string // profileimageurl
	profileimageurlsmall string // profileimageurlsmall
}
usercompetency **Optional** // 
{
	userid int // userid
	competencyid int // competencyid
	status int // status
	reviewerid int // reviewerid
	proficiency int // proficiency
	grade int // grade
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	canrequestreview int // canrequestreview
	canreview int // canreview
	gradename string // gradename
	isrequestreviewallowed int // isrequestreviewallowed
	iscancelreviewrequestallowed int // iscancelreviewrequestallowed
	isstartreviewallowed int // isstartreviewallowed
	isstopreviewallowed int // isstopreviewallowed
	isstatusidle int // isstatusidle
	isstatusinreview int // isstatusinreview
	isstatuswaitingforreview int // isstatuswaitingforreview
	proficiencyname string // proficiencyname
	reviewer **Optional** // 
	{
		id int // id
		email string // email
		idnumber string // idnumber
		phone1 string // phone1
		phone2 string // phone2
		department string // department
		institution string // institution
		fullname string // fullname
		identity string // identity
		profileurl string // profileurl
		profileimageurl string // profileimageurl
		profileimageurlsmall string // profileimageurlsmall
	}
	statusname string // statusname
	url string // url
}
usercompetencyplan **Optional** // 
{
	userid int // userid
	competencyid int // competencyid
	proficiency int // proficiency
	grade int // grade
	planid int // planid
	sortorder int // sortorder
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	gradename string // gradename
	proficiencyname string // proficiencyname
}
usercompetencycourse **Optional** // 
{
	userid int // userid
	courseid int // courseid
	competencyid int // competencyid
	proficiency int // proficiency
	grade int // grade
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	gradename string // gradename
	proficiencyname string // proficiencyname
}
evidence // evidence
[
	{
		usercompetencyid int // usercompetencyid
		contextid int // contextid
		action int // action
		actionuserid int // actionuserid
		descidentifier string // descidentifier
		desccomponent string // desccomponent
		desca string // desca
		url string // url
		grade int // grade
		note string // note
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		actionuser **Optional** // 
		{
			id int // id
			email string // email
			idnumber string // idnumber
			phone1 string // phone1
			phone2 string // phone2
			department string // department
			institution string // institution
			fullname string // fullname
			identity string // identity
			profileurl string // profileurl
			profileimageurl string // profileimageurl
			profileimageurlsmall string // profileimageurlsmall
		}
		description string // description
		gradename string // gradename
		userdate string // userdate
		candelete int // candelete
	}
]
commentarea **Optional** // 
{
	component string // component
	commentarea string // commentarea
	itemid int // itemid
	courseid int // courseid
	contextid int // contextid
	cid string // cid
	autostart int // autostart
	canpost int // canpost
	canview int // canview
	count int // count
	collapsediconkey string // collapsediconkey
	displaytotalcount int // displaytotalcount
	displaycancel int // displaycancel
	fullwidth int // fullwidth
	linktext string // linktext
	notoggle int // notoggle
	template string // template
	canpostorhascomments int // canpostorhascomments
}
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_user_competency_summary_in_course</summary>
<br/>
<p>Load a summary of a user competency.</p>
<h3>Parameters</h3>
```
userid int // Data base record id for the user
competencyid int // Data base record id for the competency
courseid int // Data base record id for the course
```

<h3>Returns</h3>
```
usercompetencysummary // 
{
	showrelatedcompetencies int // showrelatedcompetencies
	cangrade int // cangrade
	competency // 
	{
		linkedcourses // linkedcourses
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
		relatedcompetencies // relatedcompetencies
		[
			{
				shortname string // shortname
				idnumber string // idnumber
				description string // description
				descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				sortorder int // sortorder
				parentid int // parentid
				path string // path
				ruleoutcome int // ruleoutcome
				ruletype string // ruletype
				ruleconfig string // ruleconfig
				scaleid int // scaleid
				scaleconfiguration string // scaleconfiguration
				competencyframeworkid int // competencyframeworkid
				id int // id
				timecreated int // timecreated
				timemodified int // timemodified
				usermodified int // usermodified
			}
		]
		competency // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
		framework // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			visible int // visible
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			contextid int // contextid
			taxonomies string // taxonomies
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			canmanage int // canmanage
			competenciescount int // competenciescount
			contextname string // contextname
			contextnamenoprefix string // contextnamenoprefix
		}
		hascourses int // hascourses
		hasrelatedcompetencies int // hasrelatedcompetencies
		scaleid int // scaleid
		scaleconfiguration string // scaleconfiguration
		taxonomyterm string // taxonomyterm
		comppath // 
		{
			ancestors // ancestors
			[
				{
					id int // id
					name string // name
					first int // first
					last int // last
					position int // position
				}
			]
			framework // 
			{
				id int // id
				name string // name
				first int // first
				last int // last
				position int // position
			}
			pluginbaseurl string // pluginbaseurl
			pagecontextid int // pagecontextid
			showlinks int // showlinks
		}
		pluginbaseurl string // pluginbaseurl
	}
	user // 
	{
		id int // id
		email string // email
		idnumber string // idnumber
		phone1 string // phone1
		phone2 string // phone2
		department string // department
		institution string // institution
		fullname string // fullname
		identity string // identity
		profileurl string // profileurl
		profileimageurl string // profileimageurl
		profileimageurlsmall string // profileimageurlsmall
	}
	usercompetency **Optional** // 
	{
		userid int // userid
		competencyid int // competencyid
		status int // status
		reviewerid int // reviewerid
		proficiency int // proficiency
		grade int // grade
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		canrequestreview int // canrequestreview
		canreview int // canreview
		gradename string // gradename
		isrequestreviewallowed int // isrequestreviewallowed
		iscancelreviewrequestallowed int // iscancelreviewrequestallowed
		isstartreviewallowed int // isstartreviewallowed
		isstopreviewallowed int // isstopreviewallowed
		isstatusidle int // isstatusidle
		isstatusinreview int // isstatusinreview
		isstatuswaitingforreview int // isstatuswaitingforreview
		proficiencyname string // proficiencyname
		reviewer **Optional** // 
		{
			id int // id
			email string // email
			idnumber string // idnumber
			phone1 string // phone1
			phone2 string // phone2
			department string // department
			institution string // institution
			fullname string // fullname
			identity string // identity
			profileurl string // profileurl
			profileimageurl string // profileimageurl
			profileimageurlsmall string // profileimageurlsmall
		}
		statusname string // statusname
		url string // url
	}
	usercompetencyplan **Optional** // 
	{
		userid int // userid
		competencyid int // competencyid
		proficiency int // proficiency
		grade int // grade
		planid int // planid
		sortorder int // sortorder
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		gradename string // gradename
		proficiencyname string // proficiencyname
	}
	usercompetencycourse **Optional** // 
	{
		userid int // userid
		courseid int // courseid
		competencyid int // competencyid
		proficiency int // proficiency
		grade int // grade
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		gradename string // gradename
		proficiencyname string // proficiencyname
	}
	evidence // evidence
	[
		{
			usercompetencyid int // usercompetencyid
			contextid int // contextid
			action int // action
			actionuserid int // actionuserid
			descidentifier string // descidentifier
			desccomponent string // desccomponent
			desca string // desca
			url string // url
			grade int // grade
			note string // note
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			actionuser **Optional** // 
			{
				id int // id
				email string // email
				idnumber string // idnumber
				phone1 string // phone1
				phone2 string // phone2
				department string // department
				institution string // institution
				fullname string // fullname
				identity string // identity
				profileurl string // profileurl
				profileimageurl string // profileimageurl
				profileimageurlsmall string // profileimageurlsmall
			}
			description string // description
			gradename string // gradename
			userdate string // userdate
			candelete int // candelete
		}
	]
	commentarea **Optional** // 
	{
		component string // component
		commentarea string // commentarea
		itemid int // itemid
		courseid int // courseid
		contextid int // contextid
		cid string // cid
		autostart int // autostart
		canpost int // canpost
		canview int // canview
		count int // count
		collapsediconkey string // collapsediconkey
		displaytotalcount int // displaytotalcount
		displaycancel int // displaycancel
		fullwidth int // fullwidth
		linktext string // linktext
		notoggle int // notoggle
		template string // template
		canpostorhascomments int // canpostorhascomments
	}
}
course // 
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
coursemodules // coursemodules
[
	{
		id int // id
		name string // name
		url string **Optional** // url
		iconurl string // iconurl
	}
]
plans // plans
[
	{
		name string // name
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		userid int // userid
		templateid int // templateid
		origtemplateid int // origtemplateid
		status int // status
		duedate int // duedate
		reviewerid int // reviewerid
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		statusname string // statusname
		isbasedontemplate int // isbasedontemplate
		canmanage int // canmanage
		canrequestreview int // canrequestreview
		canreview int // canreview
		canbeedited int // canbeedited
		isactive int // isactive
		isdraft int // isdraft
		iscompleted int // iscompleted
		isinreview int // isinreview
		iswaitingforreview int // iswaitingforreview
		isreopenallowed int // isreopenallowed
		iscompleteallowed int // iscompleteallowed
		isunlinkallowed int // isunlinkallowed
		isrequestreviewallowed int // isrequestreviewallowed
		iscancelreviewrequestallowed int // iscancelreviewrequestallowed
		isstartreviewallowed int // isstartreviewallowed
		isstopreviewallowed int // isstopreviewallowed
		isapproveallowed int // isapproveallowed
		isunapproveallowed int // isunapproveallowed
		duedateformatted string // duedateformatted
		commentarea // 
		{
			component string // component
			commentarea string // commentarea
			itemid int // itemid
			courseid int // courseid
			contextid int // contextid
			cid string // cid
			autostart int // autostart
			canpost int // canpost
			canview int // canview
			count int // count
			collapsediconkey string // collapsediconkey
			displaytotalcount int // displaytotalcount
			displaycancel int // displaycancel
			fullwidth int // fullwidth
			linktext string // linktext
			notoggle int // notoggle
			template string // template
			canpostorhascomments int // canpostorhascomments
		}
		reviewer **Optional** // 
		{
			id int // id
			email string // email
			idnumber string // idnumber
			phone1 string // phone1
			phone2 string // phone2
			department string // department
			institution string // institution
			fullname string // fullname
			identity string // identity
			profileurl string // profileurl
			profileimageurl string // profileimageurl
			profileimageurlsmall string // profileimageurlsmall
		}
		template **Optional** // 
		{
			shortname string // shortname
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			duedate int // duedate
			visible int // visible
			contextid int // contextid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			duedateformatted string // duedateformatted
			cohortscount int // cohortscount
			planscount int // planscount
			canmanage int // canmanage
			canread int // canread
			contextname string // contextname
			contextnamenoprefix string // contextnamenoprefix
		}
		url string // url
	}
]
pluginbaseurl string // pluginbaseurl
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_user_competency_summary_in_plan</summary>
<br/>
<p>Load a summary of a user competency.</p>
<h3>Parameters</h3>
```
competencyid int // Data base record id for the competency
planid int // Data base record id for the plan
```

<h3>Returns</h3>
```
usercompetencysummary // 
{
	showrelatedcompetencies int // showrelatedcompetencies
	cangrade int // cangrade
	competency // 
	{
		linkedcourses // linkedcourses
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
		relatedcompetencies // relatedcompetencies
		[
			{
				shortname string // shortname
				idnumber string // idnumber
				description string // description
				descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				sortorder int // sortorder
				parentid int // parentid
				path string // path
				ruleoutcome int // ruleoutcome
				ruletype string // ruletype
				ruleconfig string // ruleconfig
				scaleid int // scaleid
				scaleconfiguration string // scaleconfiguration
				competencyframeworkid int // competencyframeworkid
				id int // id
				timecreated int // timecreated
				timemodified int // timemodified
				usermodified int // usermodified
			}
		]
		competency // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			sortorder int // sortorder
			parentid int // parentid
			path string // path
			ruleoutcome int // ruleoutcome
			ruletype string // ruletype
			ruleconfig string // ruleconfig
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			competencyframeworkid int // competencyframeworkid
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
		}
		framework // 
		{
			shortname string // shortname
			idnumber string // idnumber
			description string // description
			descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
			visible int // visible
			scaleid int // scaleid
			scaleconfiguration string // scaleconfiguration
			contextid int // contextid
			taxonomies string // taxonomies
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			canmanage int // canmanage
			competenciescount int // competenciescount
			contextname string // contextname
			contextnamenoprefix string // contextnamenoprefix
		}
		hascourses int // hascourses
		hasrelatedcompetencies int // hasrelatedcompetencies
		scaleid int // scaleid
		scaleconfiguration string // scaleconfiguration
		taxonomyterm string // taxonomyterm
		comppath // 
		{
			ancestors // ancestors
			[
				{
					id int // id
					name string // name
					first int // first
					last int // last
					position int // position
				}
			]
			framework // 
			{
				id int // id
				name string // name
				first int // first
				last int // last
				position int // position
			}
			pluginbaseurl string // pluginbaseurl
			pagecontextid int // pagecontextid
			showlinks int // showlinks
		}
		pluginbaseurl string // pluginbaseurl
	}
	user // 
	{
		id int // id
		email string // email
		idnumber string // idnumber
		phone1 string // phone1
		phone2 string // phone2
		department string // department
		institution string // institution
		fullname string // fullname
		identity string // identity
		profileurl string // profileurl
		profileimageurl string // profileimageurl
		profileimageurlsmall string // profileimageurlsmall
	}
	usercompetency **Optional** // 
	{
		userid int // userid
		competencyid int // competencyid
		status int // status
		reviewerid int // reviewerid
		proficiency int // proficiency
		grade int // grade
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		canrequestreview int // canrequestreview
		canreview int // canreview
		gradename string // gradename
		isrequestreviewallowed int // isrequestreviewallowed
		iscancelreviewrequestallowed int // iscancelreviewrequestallowed
		isstartreviewallowed int // isstartreviewallowed
		isstopreviewallowed int // isstopreviewallowed
		isstatusidle int // isstatusidle
		isstatusinreview int // isstatusinreview
		isstatuswaitingforreview int // isstatuswaitingforreview
		proficiencyname string // proficiencyname
		reviewer **Optional** // 
		{
			id int // id
			email string // email
			idnumber string // idnumber
			phone1 string // phone1
			phone2 string // phone2
			department string // department
			institution string // institution
			fullname string // fullname
			identity string // identity
			profileurl string // profileurl
			profileimageurl string // profileimageurl
			profileimageurlsmall string // profileimageurlsmall
		}
		statusname string // statusname
		url string // url
	}
	usercompetencyplan **Optional** // 
	{
		userid int // userid
		competencyid int // competencyid
		proficiency int // proficiency
		grade int // grade
		planid int // planid
		sortorder int // sortorder
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		gradename string // gradename
		proficiencyname string // proficiencyname
	}
	usercompetencycourse **Optional** // 
	{
		userid int // userid
		courseid int // courseid
		competencyid int // competencyid
		proficiency int // proficiency
		grade int // grade
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		gradename string // gradename
		proficiencyname string // proficiencyname
	}
	evidence // evidence
	[
		{
			usercompetencyid int // usercompetencyid
			contextid int // contextid
			action int // action
			actionuserid int // actionuserid
			descidentifier string // descidentifier
			desccomponent string // desccomponent
			desca string // desca
			url string // url
			grade int // grade
			note string // note
			id int // id
			timecreated int // timecreated
			timemodified int // timemodified
			usermodified int // usermodified
			actionuser **Optional** // 
			{
				id int // id
				email string // email
				idnumber string // idnumber
				phone1 string // phone1
				phone2 string // phone2
				department string // department
				institution string // institution
				fullname string // fullname
				identity string // identity
				profileurl string // profileurl
				profileimageurl string // profileimageurl
				profileimageurlsmall string // profileimageurlsmall
			}
			description string // description
			gradename string // gradename
			userdate string // userdate
			candelete int // candelete
		}
	]
	commentarea **Optional** // 
	{
		component string // component
		commentarea string // commentarea
		itemid int // itemid
		courseid int // courseid
		contextid int // contextid
		cid string // cid
		autostart int // autostart
		canpost int // canpost
		canview int // canview
		count int // count
		collapsediconkey string // collapsediconkey
		displaytotalcount int // displaytotalcount
		displaycancel int // displaycancel
		fullwidth int // fullwidth
		linktext string // linktext
		notoggle int // notoggle
		template string // template
		canpostorhascomments int // canpostorhascomments
	}
}
plan // 
{
	name string // name
	description string // description
	descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	userid int // userid
	templateid int // templateid
	origtemplateid int // origtemplateid
	status int // status
	duedate int // duedate
	reviewerid int // reviewerid
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	statusname string // statusname
	isbasedontemplate int // isbasedontemplate
	canmanage int // canmanage
	canrequestreview int // canrequestreview
	canreview int // canreview
	canbeedited int // canbeedited
	isactive int // isactive
	isdraft int // isdraft
	iscompleted int // iscompleted
	isinreview int // isinreview
	iswaitingforreview int // iswaitingforreview
	isreopenallowed int // isreopenallowed
	iscompleteallowed int // iscompleteallowed
	isunlinkallowed int // isunlinkallowed
	isrequestreviewallowed int // isrequestreviewallowed
	iscancelreviewrequestallowed int // iscancelreviewrequestallowed
	isstartreviewallowed int // isstartreviewallowed
	isstopreviewallowed int // isstopreviewallowed
	isapproveallowed int // isapproveallowed
	isunapproveallowed int // isunapproveallowed
	duedateformatted string // duedateformatted
	commentarea // 
	{
		component string // component
		commentarea string // commentarea
		itemid int // itemid
		courseid int // courseid
		contextid int // contextid
		cid string // cid
		autostart int // autostart
		canpost int // canpost
		canview int // canview
		count int // count
		collapsediconkey string // collapsediconkey
		displaytotalcount int // displaytotalcount
		displaycancel int // displaycancel
		fullwidth int // fullwidth
		linktext string // linktext
		notoggle int // notoggle
		template string // template
		canpostorhascomments int // canpostorhascomments
	}
	reviewer **Optional** // 
	{
		id int // id
		email string // email
		idnumber string // idnumber
		phone1 string // phone1
		phone2 string // phone2
		department string // department
		institution string // institution
		fullname string // fullname
		identity string // identity
		profileurl string // profileurl
		profileimageurl string // profileimageurl
		profileimageurlsmall string // profileimageurlsmall
	}
	template **Optional** // 
	{
		shortname string // shortname
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		duedate int // duedate
		visible int // visible
		contextid int // contextid
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		duedateformatted string // duedateformatted
		cohortscount int // cohortscount
		planscount int // planscount
		canmanage int // canmanage
		canread int // canread
		contextname string // contextname
		contextnamenoprefix string // contextnamenoprefix
	}
	url string // url
}
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_user_evidence_list_page</summary>
<br/>
<p>Load the data for the user evidence list page template</p>
<h3>Parameters</h3>
```
userid int // The user ID
```

<h3>Returns</h3>
```
canmanage int // Can the current user manage the user's evidence
userid int // The user ID
pluginbaseurl string // Url to the tool_lp plugin folder on this Moodle site
evidence // 
[
	{
		userid int // userid
		name string // name
		description string // description
		descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
		url string // url
		id int // id
		timecreated int // timecreated
		timemodified int // timemodified
		usermodified int // usermodified
		canmanage int // canmanage
		filecount int // filecount
		files // files
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
		hasurlorfiles int // hasurlorfiles
		urlshort string // urlshort
		competencycount int // competencycount
		usercompetencies **Optional** // usercompetencies
		[
			{
				competency // 
				{
					shortname string // shortname
					idnumber string // idnumber
					description string // description
					descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
					sortorder int // sortorder
					parentid int // parentid
					path string // path
					ruleoutcome int // ruleoutcome
					ruletype string // ruletype
					ruleconfig string // ruleconfig
					scaleid int // scaleid
					scaleconfiguration string // scaleconfiguration
					competencyframeworkid int // competencyframeworkid
					id int // id
					timecreated int // timecreated
					timemodified int // timemodified
					usermodified int // usermodified
				}
				usercompetency // 
				{
					userid int // userid
					competencyid int // competencyid
					status int // status
					reviewerid int // reviewerid
					proficiency int // proficiency
					grade int // grade
					id int // id
					timecreated int // timecreated
					timemodified int // timemodified
					usermodified int // usermodified
					canrequestreview int // canrequestreview
					canreview int // canreview
					gradename string // gradename
					isrequestreviewallowed int // isrequestreviewallowed
					iscancelreviewrequestallowed int // iscancelreviewrequestallowed
					isstartreviewallowed int // isstartreviewallowed
					isstopreviewallowed int // isstopreviewallowed
					isstatusidle int // isstatusidle
					isstatusinreview int // isstatusinreview
					isstatuswaitingforreview int // isstatuswaitingforreview
					proficiencyname string // proficiencyname
					reviewer **Optional** // 
					{
						id int // id
						email string // email
						idnumber string // idnumber
						phone1 string // phone1
						phone2 string // phone2
						department string // department
						institution string // institution
						fullname string // fullname
						identity string // identity
						profileurl string // profileurl
						profileimageurl string // profileimageurl
						profileimageurlsmall string // profileimageurlsmall
					}
					statusname string // statusname
					url string // url
				}
			}
		]
		userhasplan int // userhasplan
	}
]
navigation // 
[
	{
		string // HTML for a navigation item that should be on this page
	}
]
```

<hr/>
</details>
<details>
<summary>tool_lp_data_for_user_evidence_page</summary>
<br/>
<p>Load the data for the user evidence page template</p>
<h3>Parameters</h3>
```
id int // The user evidence ID
```

<h3>Returns</h3>
```
userevidence // 
{
	userid int // userid
	name string // name
	description string // description
	descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
	url string // url
	id int // id
	timecreated int // timecreated
	timemodified int // timemodified
	usermodified int // usermodified
	canmanage int // canmanage
	filecount int // filecount
	files // files
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
	hasurlorfiles int // hasurlorfiles
	urlshort string // urlshort
	competencycount int // competencycount
	usercompetencies **Optional** // usercompetencies
	[
		{
			competency // 
			{
				shortname string // shortname
				idnumber string // idnumber
				description string // description
				descriptionformat int // description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
				sortorder int // sortorder
				parentid int // parentid
				path string // path
				ruleoutcome int // ruleoutcome
				ruletype string // ruletype
				ruleconfig string // ruleconfig
				scaleid int // scaleid
				scaleconfiguration string // scaleconfiguration
				competencyframeworkid int // competencyframeworkid
				id int // id
				timecreated int // timecreated
				timemodified int // timemodified
				usermodified int // usermodified
			}
			usercompetency // 
			{
				userid int // userid
				competencyid int // competencyid
				status int // status
				reviewerid int // reviewerid
				proficiency int // proficiency
				grade int // grade
				id int // id
				timecreated int // timecreated
				timemodified int // timemodified
				usermodified int // usermodified
				canrequestreview int // canrequestreview
				canreview int // canreview
				gradename string // gradename
				isrequestreviewallowed int // isrequestreviewallowed
				iscancelreviewrequestallowed int // iscancelreviewrequestallowed
				isstartreviewallowed int // isstartreviewallowed
				isstopreviewallowed int // isstopreviewallowed
				isstatusidle int // isstatusidle
				isstatusinreview int // isstatusinreview
				isstatuswaitingforreview int // isstatuswaitingforreview
				proficiencyname string // proficiencyname
				reviewer **Optional** // 
				{
					id int // id
					email string // email
					idnumber string // idnumber
					phone1 string // phone1
					phone2 string // phone2
					department string // department
					institution string // institution
					fullname string // fullname
					identity string // identity
					profileurl string // profileurl
					profileimageurl string // profileimageurl
					profileimageurlsmall string // profileimageurlsmall
				}
				statusname string // statusname
				url string // url
			}
		}
	]
	userhasplan int // userhasplan
}
pluginbaseurl string // Url to the tool_lp plugin folder on this Moodle site
```

<hr/>
</details>
<details>
<summary>tool_mobile_call_external_functions</summary>
<br/>
<p>Call multiple external functions and return all responses.</p>
<h3>Parameters</h3>
```
requests // 
[
	{
		function string // Function name
		arguments string // JSON-encoded object with named arguments
		settingraw int // Return raw text
		settingfilter int // Filter text
		settingfileurl int // Rewrite plugin file URLs
		settinglang string // Session language
	}
]
```

<h3>Returns</h3>
```
responses // 
[
	{
		error int // Whether an exception was thrown.
		data string **Optional** // JSON-encoded response data
		exception string **Optional** // JSON-encoed exception info
	}
]
```

<hr/>
</details>
<details>
<summary>tool_mobile_get_autologin_key</summary>
<br/>
<p>Creates an auto-login key for the current user.
                            Is created only in https sites and is restricted by time, ip address and only works if the request
                            comes from the Moodle mobile or desktop app.</p>
<h3>Parameters</h3>
```
privatetoken string // Private token, usually generated by login/token.php
```

<h3>Returns</h3>
```
key string // Auto-login key for a single usage with time expiration.
autologinurl string // Auto-login URL.
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
<summary>tool_mobile_get_config</summary>
<br/>
<p>Returns a list of the site configurations, filtering by section.</p>
<h3>Parameters</h3>
```
section string // Settings section name.
```

<h3>Returns</h3>
```
settings // Settings
[
	{
		name string // The name of the setting
		value string // The value of the setting
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
<summary>tool_mobile_get_content</summary>
<br/>
<p>Returns a piece of content to be displayed in the Mobile app.</p>
<h3>Parameters</h3>
```
component string // Component where the class is e.g. mod_assign.
method string // Method to execute in class \$component\output\mobile.
args **Optional** // Args for the method are optional.
[
	{
		name string // Param name.
		value string // Param value.
	}
]
```

<h3>Returns</h3>
```
templates // Templates required by the generated content.
[
	{
		id string // ID of the template.
		html string // HTML code.
	}
]
javascript string // JavaScript code.
otherdata // Other data that can be used or manipulated by the template via 2-way data-binding.
[
	{
		name string // Field name.
		value string // Field value.
	}
]
files // Files in the content.
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
restrict // Restrict this content to certain users or courses.
{
	users **Optional** // List of allowed users.
	[
		{
		int // user id
		}
	]
	courses **Optional** // List of allowed courses.
	[
		{
		int // course id
		}
	]
}
disabled int **Optional** // Whether we consider this disabled or not.
```

<hr/>
</details>
<details>
<summary>tool_mobile_get_plugins_supporting_mobile</summary>
<br/>
<p>Returns a list of Moodle plugins supporting the mobile app.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
plugins // 
[
	{
		component string // The plugin component name.
		version string // The plugin version number.
		addon string // The Mobile addon (package) name.
		dependencies // The list of Mobile addons this addon depends on.
		[
			{
		string // Mobile addon name.
			}
		]
		fileurl string // The addon package url for download
                                                            or empty if it doesn't exist.
		filehash string // The addon package hash or empty if it doesn't exist.
		filesize int // The addon package size or empty if it doesn't exist.
		handlers string **Optional** // Handlers definition (JSON)
		lang string **Optional** // Language strings used by the handlers (JSON)
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
<summary>tool_mobile_get_public_config</summary>
<br/>
<p>Returns a list of the site public settings, those not requiring authentication.</p>
<h3>Parameters</h3>
<strong>No Parameters.</strong><br/>

<h3>Returns</h3>
```
wwwroot string // Site URL.
httpswwwroot string // Site https URL (if httpslogin is enabled).
sitename string // Site name.
guestlogin int // Whether guest login is enabled.
rememberusername int // Values: 0 for No, 1 for Yes, 2 for optional.
authloginviaemail int // Whether log in via email is enabled.
registerauth string // Authentication method for user registration.
forgottenpasswordurl string // Forgotten password URL.
authinstructions string // Authentication instructions.
authnoneenabled int // Whether auth none is enabled.
enablewebservices int // Whether Web Services are enabled.
enablemobilewebservice int // Whether the Mobile service is enabled.
maintenanceenabled int // Whether site maintenance is enabled.
maintenancemessage string // Maintenance message.
logourl string **Optional** // The site logo URL
compactlogourl string **Optional** // The site compact logo URL
typeoflogin int // The type of login. 1 for app, 2 for browser, 3 for embedded.
launchurl string **Optional** // SSO login launch URL.
mobilecssurl string **Optional** // Mobile custom CSS theme
tool_mobile_disabledfeatures string **Optional** // Disabled features in the app
identityproviders **Optional** // Identity providers
[
	{
		name string // The identity provider name.
		iconurl string // The icon URL for the provider.
		url string // The URL of the provider.
	}
]
country string **Optional** // Default site country
agedigitalconsentverification int **Optional** // Whether age digital consent verification
                    is enabled.
supportname string **Optional** // Site support contact name
                    (only if age verification is enabled).
supportemail string **Optional** // Site support contact email
                    (only if age verification is enabled).
autolang int **Optional** // Whether to detect default language
                    from browser setting.
lang string **Optional** // Default language for the site.
langmenu int **Optional** // Whether the language menu should be displayed.
langlist string **Optional** // Languages on language menu.
locale string **Optional** // Sitewide locale.
tool_mobile_minimumversion string **Optional** // Minimum required version to access.
tool_mobile_iosappid string **Optional** // iOS app's unique identifier.
tool_mobile_androidappid string **Optional** // Android app's unique identifier.
tool_mobile_setuplink string **Optional** // App download page.
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
<summary>tool_mobile_get_tokens_for_qr_login</summary>
<br/>
<p>Returns a WebService token (and private token) for QR login.</p>
<h3>Parameters</h3>
```
qrloginkey string // The user key for validating the request.
userid int // The user the key belongs to.
```

<h3>Returns</h3>
```
token string // A valid WebService token for the official mobile app service.
privatetoken string // Private token used for auto-login processes.
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
<summary>tool_mobile_validate_subscription_key</summary>
<br/>
<p>Check if the given site subscription key is valid.</p>
<h3>Parameters</h3>
```
key string // Site subscription temporary key.
```

<h3>Returns</h3>
```
validated int // Whether the key is validated or not.
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
<summary>tool_moodlenet_search_courses</summary>
<br/>
<p>For some given input search for a course that matches</p>
<h3>Parameters</h3>
```
searchvalue string // search value
```

<h3>Returns</h3>
```
courses // 
[
	{
		id int // course id
		fullname string // course full name
		hidden int // is the course visible
		viewurl string // Next step of import
		coursecategory string // Category name
		courseimage string // course image
	}
]
```

<hr/>
</details>
<details>
<summary>tool_moodlenet_verify_webfinger</summary>
<br/>
<p>Verify if the passed information resolves into a WebFinger profile URL</p>
<h3>Parameters</h3>
```
profileurl string // The profile url that the user has given us
course int // The course we are adding to
section int // The section within the course we are adding to
```

<h3>Returns</h3>
```
result int // Was the passed content a valid WebFinger?
message string // Our message for the user
domain string **Optional** // Domain to redirect the user to
```

<hr/>
</details>

