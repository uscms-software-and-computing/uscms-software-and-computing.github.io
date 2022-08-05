---
permalink: /docs/intern.html
layout: default
title: Information to add or update interns
pagetype: doc
---

### Adding a New Intern Page

#### USCMS Software & Computing website
In order to add your information, we request you to please supply a photo ( First_Name-Last_Name.jpg or .png - 320x240 pixels) and a paragraph summarizing your project’s goals.

You should submit a pull request with the photo, a markdown file with the summary information above, and your proposal to this repo:

<https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io>

* Add a photo named `First-Last.jpg` or `.png` to the [assets/images/team folder](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io/tree/master/assets/images/team). It should be 320x240 pixels.
* Add a pdf of your proposal named `First-Last.pdf` to the [assets/pdfs folder](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io/tree/master/assets/pdfs).
* Add a "`<your github username>.md`" file to the [interns folder in the website repository](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io/tree/master/pages/interns). Here is an example:

*Please Note*:  In the markdown file you create, ensure you set the “active” attribute to True – (i.e.  active: True).  Otherwise, your entry will not appear on our Fellows page.

Be sure to include your project summary in the project_goal field.

You can leave the “presentations” and “current_status” fields blank for now.  (Make sure to include the fields)

```yml

---
layout: intern
pagetype: intern
shortname: <your GitHub user id>
permalink: /fellows/<your GitHub user id>.html
fellow-name: <Your Name>
title: <Your Name> - USCMS S&C Intern
active: True
dates:
  start: <start date>
  end: <end date>
photo: /assets/images/team/<First name>-<Last name>.jpg
institution: <Your institution>
e-mail: <Your email>
project_title: <Project title>
project_goal: >
    Short description of your project
mentors:
  - <Mentor Name - (<Mentor Institution>)>

proposal: /assets/pdf/<find-your-file>
presentations:
  - title: "<Presentation Title"
    date: "Presentation Date"
    url: <Presentation materials link>
    meeting: <Meeting name>
    meetingurl: <Meeting url - indico link, etc.>
    recordingurl: <Recording url> (Optional)
current_status: >
  A placeholder for status updates
github-username: <Your git-hub username>
gitlab-url: <URL for your GitLab repo> (Optional)
---
```

### Dates
Date format for start and end dates should be -- YYYY-MM-DD -- i.e. 2021-12-31

### Presentations

The meaning of the fields is the following:

  * title - the title of the talk: you made need to place it in double quotes, if certain characters like a colon (":") are included in the title
  * date - the date on which the presentation was made, in the numeric format "YYYY-MM-DD"
  * url - this should be a direct URL to the presentation or page containing the presentation. For Indico, link to the contribution, not the PDF or other links.
  * meeting - the name of the meeting
  * meetingurl - the URL for the meeting in which the presentation was made
