# Jupyter 简介

Jupyter 项目的存在是为了开发开源软件、开放标准和跨数十种编程语言的交互式计算服务。

- Jupyter 支持超过 40 种编程语言，包括 Python、R、Julia 和 Scala。
- 笔记本可以通过电子邮件、Dropbox、GitHub 和 {term}`Jupyter Notebook Viewer` 与他人共享。
- 代码可以产生丰富的交互式输出：HTML、图像、视频、LaTeX 和自定义 MIME 类型。
- 利用 Python、R 和 Scala 等大数据工具，如 Apache Spark。使用 pandas, scikit-learn, ggplot2, TensorFlow 来探索相同的数据。

## JupyterLab：Jupyter 下一代笔记本接口

{term}`JupyterLab` 是一个基于 web 的交互式开发环境，用于处理 Jupyter 笔记本、代码和数据。JupyterLab 是灵活的：配置和安排用户界面，以支持数据科学、科学计算和机器学习的广泛工作流。JupyterLab 是可扩展和模块化的：编写添加新组件并与现有组件集成的插件。

## Jupyter Notebook

{term}`Jupyter Notebook` 是一个开源的网络应用程序，允许你创建和共享包含实时代码、方程式、可视化和叙事文本的文档。用途包括：数据清理和转换，数值模拟，统计建模，数据可视化，机器学习，等等。

## JupyterHub

{term}`JupyterHub` 是一款专为公司、课堂和研究实验室设计的多用户版本的笔记本。

- **可拔插的身份验证**：使用 PAM、OAuth 管理用户和身份验证，或者与您自己的目录服务系统集成。
- **中心化部署**：在站点内或站点外的集中基础设施上，将 Jupyter Notebook 部署到组织内的数千名用户。
- **友好的容器**：使用 Docker 和 Kubernetes 扩展您的部署，隔离用户进程，并简化软件安装。
- **代码与数据**：将 Notebook 部署在数据旁边，以便在组织内提供统一的软件管理和数据访问。

## 与 Voilà 交流你的结果

Voilà 帮助您与用户沟通见解，通过将一个 Jupyter 笔记本转换成一个独立的 web 应用程序，您可以分享。它让您可以在一个安全且可定制的交互式仪表板中控制读者的体验。

## 交互式计算的开放标准

Jupyter Notebook 基于一套交互式计算的开放标准。借助 HTML 和 CSS 在网络上的交互式计算。第三方开发人员可以利用这些开放标准来构建带有嵌入式交互式计算的定制应用程序。

- NB（Notebok Document Format ）：Jupyter Notebook 是一种基于 JSON 的开放文档格式。它们包含用户会话的完整记录，包括代码、叙述文本、方程式和丰富的输出。
- **交互式计算协议**：Notebook 使用交互式计算协议（Interactive Computing Protocol）与计算内核通信，交互式计算协议是一种基于 ZMQ 和 WebSockets 上的 JSON 数据的开放网络协议。
- **内核**是用特定编程语言运行交互代码并向用户返回输出的进程。内核还响应 Tab 补全和自省请求。

## Jupyter 组织

Jupyter 项目开发的软件是在 BSD（或类似的）开源许可下发布的，公开开发并托管在 [IPython GitHub 组织](https://github.com/ipython) 和 [Jupyter GitHub组织](https://github.com/jupyter) 下的公共 GitHub 库中。项目软件的例子包括  [Jupyter](https://jupyter.org)，[IPython](https://ipython.org)，[nbviewer](https://nbviewer.ipython.org) 和 [Jupyter coLaboratory](https://colaboratory.jupyter.org)。


以下 GitHub 上的组织包含项目 Jupyter 项目：

- [jupyter](https://github.com/jupyter)
- [ipython](https://github.com/ipython)
- [jupyterhub](https://github.com/jupyterhub)
- [jupyterlab](https://github.com/jupyterlab)
- [jupyter-widgets](https://github.com/jupyter-widgets)
- [jupyter-server](https://github.com/jupyter-server)
- [jupyter-xeus](https://github.com/jupyter-xeus)
- [voila-dashboards](https://github.com/voila-dashboards)
- [binder-examples](https://github.com/binder-examples)
- [jupyter-resources](https://github.com/jupyter-resources)
