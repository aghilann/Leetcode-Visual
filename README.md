<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Leetcode Visualizer</h3>

  <p align="center">
    From Aghilan Nathan
    <br />
    <br />
    <br />
    <a href="https://leetcode-visual.herokuapp.com/">Production Site</a>
    ·
    <a href="mailto:nathanaghilan@gmail.com">Report Bug</a>
    ·
    <a href="mailto:nathanaghilan@gmail.com">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The goal of this project is to visualize your strengths and weaknesses when it comes to solving Data Structures,
the main page includes various bar graphs for each Data Structure so you can visually see where your strengths and weakness lie. 
We created this site as feature we would like to see implented on LeetCode, they allow you to view the questions you have solved but not in such an organized manner.
In an ideal scenario, a user should not have to manually input the questions they have solved and an API would actually do the task automatically. 

This project was created as apart of nwHacks 2022 on January 14th. 
I spent 9 hours creating the backend and ensuring the data being sent to the HTML pages in the front end.
Another 4 hours was spent displaying the data and replacing the dummy data in the current HTML and mostly helping with the UI.
The final hour right before the deadline was spent deployoing the site, which was done in about 10 minutes on Heroku, since I had recently deployed another project on Heroku, I was familar with the process.
The rest of the hour was spent fixing bugs, I ensured the production site had Continous Integration and Deployment for this very reason.
Even at the point of submission, we had numerous flaws in the front end I was unable to solve in time, such as the horrible and hard to see colors of the loading page.
I am very proud of what me and my team were able to get done in a short period of time with 0 preperation, I plan on spending a day when I get the chance to fix the bugs and tweak elements of the UI, there are very big things we could change that would make the project better that we did not get to because of the deadline.
We submitted with 2 minutes to spare.

Our submission is not perfect, or anywhere close to it but it taught me many valauble lessons. Suprisingly, my biggest takeways were not actually coding related, it was the soft skills I imporved upon. 
This intense and demanding Hackathon taught me key lessons such as what tasks you should delegate and what you should do yourself, how to work under heavy deadlines as well as ensuring the team was in track and knew what they were doing. 

<img width="581" alt="image" src="https://user-images.githubusercontent.com/90127404/149838903-4393b217-7cd6-4a97-ab4b-42f6aaaceeea.png">


[YouTube Video explaining the project submission](https://www.youtube.com/watch?v=zlDN6rarDLI)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLite3](https://www.sqlite.org/index.html)
* [Bootstrap](https://getbootstrap.com/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- Template Inheritance from layout.html
- User Registration and Login Forms
- User Registration and Login Information saved to SQLite3 via SQL-Alchemy ORM
- Blueprints and Configuration
- Implementation of completed back-end to existing front-end made by the rest of the team.
- Deployment of Site on Heroku via GitHub repository to allow for CI/CD

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The set up for this project is quite simple, just download or clone this repository.

### Prerequisites

I will assume you already have a version of Python greater then 3.6 installed.
  ```sh
  pip install flask
  ```
  ```sh
   pip install requirements.txt
  ```
All other dependies are listed within the requirements.txt file, you can download them all at once using the command list above.

### Installation

1. Install or Clone this repository.
2. Run app.py with a compatible version of Python 
3. Have fun!


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Project Link: [https://leetcode-visual.herokuapp.com/](https://leetcode-visual.herokuapp.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Kevin Tan - What a absolute legend coming in clutch with the animated bar graphs, even though you a very new to HTML/CSS you were willing to bit off more then you could chew, and in response you increased your capabillties and did the job to a high standard. Excellent Job, I look forward to the next Hackathon. It is gennuinly a miracle we got this done considering our knowledge and extremely low level of experience.

* Benny Chinvanich - I apologize for you having to flip flop around so much and constantly learning things, I know you had various roles and were forced to be all over the place. I thank you for your versatility.

* Rissa - You and Kevin designed the only parts of the UI that did not look horrible, it was unfortunate not everything made it in but I greatly appreciate the work you did in CSS that ensured the bar graph was successful. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/aghilan-nathan-3b65bb211/
[product-screenshot]: images/screenshot.png
