# JTISS API Documentation

## GET `/api/course/:number-:semester`
**Description:**
Get course information for a given courseNumber and semester. Only courses visible to the public will be returned.

### Parameters
| Name       | Type | Data Type | Description                                   |
|:-----------|:-----|:----------|:----------------------------------------------|
| `number`   | path | string    | Number (without dots) of the requested course |
| `semester` | path | string    | Requested semester                            |

### Responses
| Status  | Description                                          |
|:--------|:-----------------------------------------------------|
| **200** | A description of the requested course                |
| **400** | Missing courseNumber or semester parameter           |
| **404** | No course with this number in the requested semester |

---

## GET `/api/course/:number/examDates`
**Description:**
Gets a list of future exam dates for a specific course. If date is specified, all exams after that date are returned.

### Parameters
| Name       | Type  | Data Type | Description                                   |
|:-----------|:------|:----------|:----------------------------------------------|
| `number`   | path  | string    | Number (without dots) of the requested course |
| `fromDate` | query | string    | Date in format yyyy-MM-dd                     |

### Responses
| Status  | Description                                          |
|:--------|:-----------------------------------------------------|
| **200** | List of future exam dates for a specific course      |
| **400** | Missing courseNumber                                 |
| **404** | No course with this number found/No exams were found |

---

## GET `/api/course/hasPublic/lecturer/tissId/:tissId`
**Description:**
Check for public courses by lecturer TISS ID.

### Parameters
| Name     | Type | Data Type | Description             |
|:---------|:-----|:----------|:------------------------|
| `tissId` | path | string    | Tiss ID of the lecturer |

### Responses
| Status  | Description    |
|:--------|:---------------|
| **200** | Success        |
| **400** | Missing TissId |

---

## GET `/api/course/hasPublic/orgUnit/:orgUnitCode`
**Description:**
Check for public courses by Organizational Unit Code.

### Parameters
| Name          | Type | Data Type | Description                     |
|:--------------|:-----|:----------|:--------------------------------|
| `orgUnitCode` | path | string    | Code of the Organizational Unit |

### Responses
| Status  | Description           |
|:--------|:----------------------|
| **200** | Success               |
| **400** | Invalid semester code |

---

## GET `/api/course/lecturer/:oid`
**Description:**
Get a list of courses offered by a lecturer in a given semester. Only courses visible to the public will be returned.

### Parameters
| Name       | Type  | Data Type | Description                  |
|:-----------|:------|:----------|:-----------------------------|
| `oid`      | path  | string    | OID referencing the lecturer |
| `semester` | query | string    | Requested semester           |

### Responses
| Status  | Description                                                                      |
|:--------|:---------------------------------------------------------------------------------|
| **200** | A list of publicly visible courses offered by the lecturer in the given semester |
| **400** | Invalid semester code / No person with the given OID was found                   |

---

## GET `/api/course/orgUnit/:code`
**Description:**
Get all courses offered by an org unit in a given semester. Only courses visible to the public will be returned.

### Parameters
| Name       | Type  | Data Type | Description          |
|:-----------|:------|:----------|:---------------------|
| `code`     | path  | string    | Code of the org unit |
| `semester` | query | string    | Requested semester   |

### Responses
| Status  | Description                                                                     |
|:--------|:--------------------------------------------------------------------------------|
| **200** | A list of publicly visible courses offered by the orgUnit in the given semester |
| **400** | Invalid semester code / Invalid org unit code                                   |

---

## GET `/api/event`
**Description:**
Get all public event dates based on the filter parameters. This mirrors the data from the public Room Booking Schedule.

### Parameters
| Name           | Type  | Data Type | Description                                                                                                         |
|:---------------|:------|:----------|:--------------------------------------------------------------------------------------------------------------------|
| `buildingCode` | query | string    | (Optional) Filter by building code                                                                                  |
| `from`         | query | string    | (Optional) Filter by date string in ISO 8601 date format 'yyyy-MM-dd' in time zone Europe/Vienna. Default: today    |
| `roomNumber`   | query | string    | (Optional) Filter by room number                                                                                    |
| `to`           | query | string    | (Optional) Filter by date string in ISO 8601 date format 'yyyy-MM-dd' in time zone Europe/Vienna. Default: tomorrow |
| `type`         | query | string    | (Optional) Filter by type of the event. Possible values: COURSE, GROUP, EXAM, OTHER, ORG, ROOM_TU_LEARN             |

### Responses
| Status  | Description                                                                 |
|:--------|:----------------------------------------------------------------------------|
| **200** | List of EventDateJson objects                                               |
| **400** | Invalid format of date parameters / Invalid date range / Unknown event type |
| **404** | No room for roomNumber is found / No building for buildingCode is found     |