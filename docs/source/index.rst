.. 多语言主文档

.. include:: ../README.md
    :parser: myst_parser.sphinx_

.. only:: zh_CN

    .. toctree::
        :maxdepth: 2
        :caption: 中文文档
        
        zh_CN/快速开始 <zh_CN/examples/overview>
        zh_CN/API文档 <zh_CN/api/index>

.. only:: en

    .. toctree::
        :maxdepth: 2
        :caption: English Docs
        
        en/Getting Started <en/examples/overview>
        en/API Reference <en/api/index>

.. autosummary::
    :toctree: _autosummary
    :template: custom_module.rst

    mcsmapi
    mcsmapi.models