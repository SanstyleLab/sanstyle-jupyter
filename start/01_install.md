# 安装 Jupyter 软件

在你的电脑上使用木星实验室或经典的 Jupyter 笔记本，只需几分钟。

```{attention}
如果你还没有安装 `mamba` 或 `conda`，你可以从 [miniforge](https://github.com/conda-forge/miniforge#mambaforge) 发行版开始。
```

`````{tabbed} JupyterLab
[安装指南](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)包含更详细的说明。

````{panels}
可以使用 `mamba` 和 `conda` 安装：
^^^

```sh
mamba install -c conda-forge jupyterlab
```

或者

```sh
conda install -c conda-forge jupyterlab
```
---

也可以使用 `pip` 安装：
^^^
```sh
pip install jupyterlab
```
+++
如果使用 `pip install --user` 进行安装，则必须将用户级 `bin` 目录添加到 `PATH` 环境变量中，以便启动 `jupyter lab`。如果你使用的是 Unix 衍生工具（FreeBSD, GNU / Linux, OS X），你可以使用 `export PATH="$HOME/.local/bin:$PATH"` 命令来实现这一点。
````

安装完成后，启动 JupyterLab：

```sh
jupyter-lab
```
`````

`````{tabbed} Jupyter Notebook
````{panels}
可以使用 `mamba` 和 `conda` 安装：
^^^

```sh
mamba install -c conda-forge notebook
```

或者

```sh
conda install -c conda-forge notebook
```
---

也可以使用 `pip` 安装：
^^^
```sh
pip install notebook
```
````

安装完成后，启动 Jupyter Notebook：

```sh
jupyter notebook
```
有关更多细节，请参见[运行笔记本](https://jupyter.readthedocs.io/en/latest/running.html#running)。
`````

`````{tabbed} Voilà
````{panels}
可以使用 `mamba` 和 `conda` 安装：
^^^

```sh
mamba install -c conda-forge voila
```

或者

```sh
conda install -c conda-forge voila
```
+++
有关更详细的说明，请查阅[安装指南](https://voila.readthedocs.io/en/stable/install.html)。
---

也可以使用 `pip` 安装：
^^^
```sh
pip install voila
```
````
`````