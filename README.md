<br />
  <h3 align="center">Blackwell Strategy</h3>

  <p align="center">
    Algorithm based on Blackwell's approachability theory used for regret minimization in strategic games
    <br />
    <a href="https://github.com/omar-bfs/Blackwell-Strategy"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/omar-bfs/Blackwell-Strategy">View Demo</a>
    ·
    <a href="https://github.com/omar-bfs/Blackwell-Strategy/issues">Report Bug</a>
    ·
    <a href="https://github.com/omar-bfs/Blackwell-Strategy/issues">Request Feature</a>
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


Blackwell proved in *An analog of the minimax theorem for vector payoffs*, (1965), the existence of a “no-regret” algorithm for a wide class of simple online learning problems involving multi-objective optimization.
In the project, we implement such an algorithm making use of the celebrated Blackwell Approachability Theorem for two-player games with player's regrets as vector quantities. More specifically, at each round, players deploy mixed strategies that are derived from the stationary distribution of the regret matrices. This procedure verifies Blackwell condition and allows players' regrets to approach the negative orthant, thus minimizing them. This method guarantees that the empirical distributions of play converge to the set of correlated equilibria of the stage game. For more details, see *A Simple Adaptive Procedure Leading to Correlated Equilibrium* (2000), Hart & Mas-Colell.


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
* [tqdm](https://pypi.org/project/tqdm/)
* [qe](https://pypi.org/project/qe/)

These can all be installed with pip, e.g.,  
```sh
  pip install nashpy
  ```

### Execution
Run the command: ```python3  BlackwellStrategy.py```

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

Project Link: [https://github.com/oboufous/Blackwell-Strategy](https://github.com/omar-bfs/Blackwell-Strategy)

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

