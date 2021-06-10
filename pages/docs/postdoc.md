---
permalink: /docs/postdoc.html
layout: default
title: Information to add or update postdoc page
pagetype: doc
---

### Adding a New Fellow Page

#### US CMS S&C website
You should submit a pull request with the photo, a markdown file with the summary information above, and your proposal to this repo:

<https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io>

* Add a photo named `First-Last.jpg` or `.png` to the [assets/images/team folder](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io/tree/master/assets/images/team). It should be 320x240 pixels.
* Add a "`<your github username>.md`" file to the [fellows folder in the website repository](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io/tree/master/pages/postdocs). Here is an example:

```yml
---
layout: postdoc
pagetype: postdoc
shortname: <your GitHub user id>
permalink: /postdocs/<your GitHub user id>.html
postdoc-name: <Your Name>
title: Post-doctoral researcher
active: True
dates:
  start: <start date>
  end: <end date>
photo: /assets/images/team/<First name>-<Last name>.jpg
institution: <Your institution>
e-mail: <Your email>
project_title: <Project title>
project_goal: >
    Short descrition of your project
mentors:
  - <Mentor Name - (<Mentor Institution>)>

proposal: /assets/pdf/Fellow-<First name>-<Last name>-Proposal.pdf
presentations:
  - title: "<Presentation Title"
    date: "Presentation Date"
    url: <Presentation materials link>
    meeting: <Meeting name>
    meetingurl: <Meeting url - indico link, etc.>
    recordingurl: <Recording url> (Optional)
    focus-area: <Focus Area - ia,ssl,ssc,doma,as,osglhc>
current_status: >
  A placeholder for status updates
---
```

### Dates
Date format for start and end dates should be -- YYYY-MM-DD -- i.e. 2021-12-31

### Presentations

The meaning of the fields is the following:

  * title - the title of the talk: you made need to place it in double quotes, if certain characters like a colon (":") are included in the title
  * date - the date on which the presentation was made, in the numeric format "YYYY-MM-DD"
  * url - this should be a direct URL to the presentation file (e.g. pdf)
  * meeting - the name of the meeting
  * meetingurl - the URL for the meeting in which the presentation was made
  * focus-area - optionally list the relevant focus area for this presentation, using its short name, i.e. one of [ia,ssl,ssc,doma,as,osglhc]. Must be a yaml list if more than one is present.
