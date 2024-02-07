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

*Please Note*:  In the markdown file you create, ensure you set the “active” attribute to True – (i.e.  active: True).  Otherwise, your entry will not appear on our Interns page.

Be sure to include your project summary in the project_goal field.

You can leave the “presentations” and “current_status” fields blank for now.  (Make sure to include the fields)

Make sure to follow the format explicitly.  The file needs to include "---" characters are the top and bottom of this header section.  The tabs and spaceing are important as well.

Anything between "<>" characters should be replaced with your information without the "<>" characters (i.e. <your GitHub user id> becomes rct225, not <rct225>)

### Dates
Date format for start and end dates should be -- YYYY-MM-DD -- i.e. 2021-12-31

You can test changes to your page by following the directions found in the [README](https://github.com/uscms-software-and-computing/uscms-software-and-computing.github.io) file for the website repository.

```yml

---
layout: intern
pagetype: intern
shortname: <your GitHub user id>
permalink: /interns/<your GitHub user id>.html
intern-name: <Your Name>
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
  Short description of your project.  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae vulputate ex. Vivamus sit amet malesuada orci. Integer blandit sem non auctor convallis. Donec at suscipit arcu. Donec placerat ex blandit magna finibus ultrices. Vivamus ultrices, nunc ac sodales vehicula, ante metus ultrices quam, in euismod dolor risus eu neque. Proin auctor magna vel lacus dictum efficitur. Praesent mauris nunc, imperdiet nec hendrerit non, pulvinar vel tortor. Donec gravida ac turpis dapibus ultricies. Sed lobortis felis vel euismod fringilla.
mentors:
  - <Mentor Name - (<Mentor Institution>)>

presentations:
current_status: >
  A placeholder for status updates
github-username: <Your git-hub username>
gitlab-url: <URL for your GitLab repo> (Optional)
---
```


