<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Purpose
This repository presents the code to easily extract the data after the NWB files are created by using our python module,[sparc_to_nwb](https://github.com/lifestrugglee/sparc2nwb/blob/main/sparc_to_nwb/sparc_to_nwb.py). This module not only provides data from basic containers but also other containers and data information as well as detailed descriptions. In other words, users can easily produce further data analysis and manipulation without the concern of unfamiliarity with the NWB format. In addition, due to the diversity of data inside the NWB file, the module can dynamically generate the function to grab the container data if it's not pre-listed. If the cases are even more complicated, users still can grab the original data of NWB format from this module.

## Usage
- For the data type and the method 
2. The dependencies required to run the python script are in `requirments.txt`. Install the dependencies.
```shell
python3 -m pip install requirements.txt
```
3. Change the `standard_path` and `filename` vairables in the main function to get the data and save the nwb files respectively.
4. Run the python script.
```shell
python3 sparc_to_nwb.py
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues
