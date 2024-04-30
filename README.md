
<div id="sayuri-art" align="center">
    <br/>
    <img src="./img/sayuri-art.PNG" alt="Sayuri Art" width="768"/>
    <h3>Sayuri</h3>
</div>

## Let's ROCK!

Sayuri is a GTP-compliant go engine based on Deep Convolutional Neural Network and Monte Carlo Tree Search. Learning the game of Go without strategic knowledge from human with AlphaZero-based algorithm. She is strongly inspired by Leela Zero and KataGo. The board data structure, search algorithm and network format are borrowed from Leela Zero in the beginning. Current version follows the KataGo research, the engine supports variable komi and board size now. Some methods or reports you may see my articles (some are chinese).

* [開發日誌](https://hackmd.io/@yrHb-fKBRoyrKDEKdPSDWg/BJgfay0Yc)
* [The performance report before UEC15 (v0.6)](https://drive.google.com/file/d/1ATd_u-E-OnviczsDH8wVL0c3Q1NzUCKW/view?usp=share_link)

## Quick Start via Terminal

First, you need a executable weights. Download the old v0.6 weights [here](https://drive.google.com/drive/folders/1nawHAKHTBKEpLcizaVrK4GVDSIuVqJ-Q?usp=sharing) or last v0.7 weights [here](https://drive.google.com/drive/folders/1_wnDk50g35ekb41Eg3VcoYlSfXt-ngQl). Some description of weights and RL progression is [here](https://hackmd.io/@yrHb-fKBRoyrKDEKdPSDWg/HJew5OFci). If you want to use the older network, please use the v0.5 engine at the ```save-last-v050``` branch.

Then start the program with GTP mode via the terminal/PowerShell, please enter

    $ ./sayuri -w <weights file> -t 1 -b 1 -p 400

You will see the diagnostic verbose. If the verbose includes ```Network Verison``` information, it means you success to execute the program with GPT mode. For more arguments, please give the ```--help``` option.

    $ ./sayuri --help

## Execute Engine via Graphical Interface

Sayuri is not complete engine. You need a graphical interface for playing with her. She supports any GTP (version 2) interface application. [Sabaki](https://sabaki.yichuanshen.de/) and [GoGui](https://github.com/Remi-Coulom/gogui) are recommended because Sayuri supports some specific analysis commands. 

* Sabaki analysis mode

![sabaki-sample01](./img/sabaki-sample01.png)

* GoGui analysis commands

![gogui-sample01](./img/gogui-sample01.png)

## Build From Source

Please see this [section](./docs/COMPILE.md). If you are Windows platform, you may download the executable file from [release page](https://github.com/CGLemon/Sayuri/releases).

## Reinforcement Learning

Sayuri is a fairly fast self-play learning system for the game of Go. The current performance is apparently better than KataGo g104 which is one of fastest system in 2019s. The pictute shows the performance v0.6 versus KataGo. [Here](./bash/README.md) will describe how to build the self-play loop.

![vs-kata](./img/katavslz-sayuri.png)

## Todo

* Support NHWC format.
* Support distributed computation.
* Support KataGo analysis mode.

## Other Resources

* Go Text Protocol, [https://www.gnu.org/software/gnugo/gnugo_19.html](https://www.gnu.org/software/gnugo/gnugo_19.html)
* Leela Zero, [https://github.com/leela-zero/leela-zero](https://github.com/leela-zero/leela-zero)
* KataGo methods, [https://github.com/lightvector/KataGo/blob/master/docs/KataGoMethods.md](https://github.com/lightvector/KataGo/blob/master/docs/KataGoMethods.md)
* [YouTube](https://www.youtube.com/watch?v=82UclNrXGxg), playing with Pachi.
* Supported analysis commands, [analyze](./docs/ANALYZE.md).
* [AlphaZero 之加速演算法實作 (v0.4~v0.5)](https://hackmd.io/@yrHb-fKBRoyrKDEKdPSDWg/HJI9_p70i), describe some methods for old version.
* [Journal](./docs/JOURNAL.md)

## License

The code is released under the GPLv3, except for threadpool.h, cppattributes.h, Eigen and Fast Float, which have specific licenses mentioned in those files.

## Contact

cglemon000@gmail.com (Hung-Tse Lin)
