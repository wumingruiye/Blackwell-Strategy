<br />
  <h3 align="center">Learning By Trial And Error</h3>

  <p align="center">
    Algorithm for learning pure Nash equilibria in finite strategic games
    <br />
    <a href="https://github.com/omar-bfs/Learning-By-Trial-And-Error"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/omar-bfs/Learning-By-Trial-And-Error">View Demo</a>
    ·
    <a href="https://github.com/omar-bfs/Learning-By-Trial-And-Error/issues">Report Bug</a>
    ·
    <a href="https://github.com/omar-bfs/Learning-By-Trial-And-Error/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Execution</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The algorithm is developped based on the method proposed in the article *Learning by trial and error* (2009) by P. Young.
Players learn by trial and error if they occasionally tries out new strategies, rejecting choices that are erroneous in the sense that they do not lead to higher
payoffs. The learning rule is called interactive trial and error (ITE), implements Nash equilibrium behavior in any game with generic payoffs and at least one pure Nash equilibrium.

<!-- <img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1"> -->

### Built With
Python 3.9

<!-- GETING STARTED -->
## Getting Started

### Prerequisites 
The following python packages are needed to run the program 
* [matplotlib](https://pypi.org/project/matplotlib/)
* [nashpy](https://pypi.org/project/nashpy/)
* [numpy](https://pypi.org/project/numpy/)

These can all be installed with pip, e.g.,  
```sh
  pip install nashpy
  ```

### Execution
Run the command: ```python3  ITE.py```

<!-- CONTRIBUTING -->
## Contributing
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Omar BOUFOUS

Link to Website: [https://omarboufous.me](https://omarboufous.me)

Mail: contact@omarboufous.me

Project Link: [https://github.com/omar-bfs/Learning-By-Trial-And-Error](https://github.com/omar-bfs/Learning-By-Trial-And-Error)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/omar-bfs/Learning-By-Trial-And-Error/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

