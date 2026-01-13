JTISS
get
/api/course/:number-:semester
Get course information for a given courseNumber and semester
Beschreibung
Get course information for a given courseNumber and semester Only courses visible to the public will be returned.

Parameter
Name	Typ	Datentyp	Beschreibung
number	path	string	Number (without dots) of the requested course
semester	path	string	Requested semester
Response
HTTP Status Code	Beschreibung
200	A description of the requested course
400	Missing courseNumber or semester parameter
404	No course with this number in the requested semester
get
/api/course/:number/examDates
Gets a list of future exam dates for a specific course.
Beschreibung
Gets a list of future exam dates for a specific course. If date is specified, all exams after that date are returned.

Parameter
Name	Typ	Datentyp	Beschreibung
number	path	string	Number (without dots) of the requested course
fromDate	query	string	Date in format yyyy-MM-dd
Response
HTTP Status Code	Beschreibung
200	List of future exam dates for a specific course
400	Missing courseNumber
404	No course with this number found/No exams were found
get
/api/course/hasPublic/lecturer/tissId/:tissId
Beschreibung

Parameter
Name	Typ	Datentyp	Beschreibung
tissId	path	string	
Response
HTTP Status Code	Beschreibung
200	
400	Missing TissId
get
/api/course/hasPublic/orgUnit/:orgUnitCode
Beschreibung

Parameter
Name	Typ	Datentyp	Beschreibung
orgUnitCode	path	string	
Response
HTTP Status Code	Beschreibung
200	
400	Invalid semester code
get
/api/course/lecturer/:oid
Get a list of courses offered by a lecturer in a given semester.
Beschreibung
Get a list of courses offered by a lecturer in a given semester. Only courses visible to the public will be returned.

Parameter
Name	Typ	Datentyp	Beschreibung
oid	path	string	OID referencing the lecturer
semester	query	string	Requested semester
Response
HTTP Status Code	Beschreibung
200	A list of publicly visible courses offered by the lecturer in the given semester
400	Invalid semester code
400	No person with the given OID was found
get
/api/course/orgUnit/:code
Get all courses offered by an org unit in a given semester.
Beschreibung
Get all courses offered by an org unit in a given semester. Only courses visible to the public will be returned.

Parameter
Name	Typ	Datentyp	Beschreibung
code	path	string	Code of the org unit
semester	query	string	Requested semester
Response
HTTP Status Code	Beschreibung
200	A list of publicly visible courses offered by the orgUnit in the given semester
400	Invalid semester code
400	Invalid org unit code
get
/api/event
Get all public event dates based on the filter parameters. This mirrors the data from the public Room Booking Schedule.
Beschreibung
Get all public event dates based on the filter parameters. This mirrors the data from the public Room Booking Schedule.

Parameter
Name	Typ	Datentyp	Beschreibung
buildingCode	query	string	optional, filter by building code
from	query	string	optional, filter by date string in ISO 8601 date format 'yyyy-MM-dd' in time zone Europe/Vienna, default today
roomNumber	query	string	optional, filter by room number
to	query	string	optional, filter by date string in ISO 8601 date format 'yyyy-MM-dd' in time zone Europe/Vienna, default tomorrow
type	query	string	optional, filter by type of the event. Possible values: COURSE, GROUP, EXAM, OTHER, ORG, ROOM_TU_LEARN.
Response
HTTP Status Code	Beschreibung
200	list of EventDateJson
400	Invalid format of date parameters
400	Invalid date range
400	Unknown event type
404	No room for roomNumber is found
404	No building for buildingCode is found
