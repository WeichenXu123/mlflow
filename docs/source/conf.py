#
# MLflow documentation build configuration file, created by
# cookiecutter pipproject
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("."))

import languagesections
from docutils.nodes import Text
from sphinx.addnodes import pending_xref

import mlflow

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_click.ext",
    "sphinx_tabs.tabs",
    "testcode_block",
    "nbsphinx",
    "sphinx_reredirects",
]

# Redirects definition in the form of ``("source", "target")``.
# Note that the target is relative to the path of the source and that the
# target must define the final url (i.e. no trailing slash).
redirects = {
    "registry": "model-registry.html",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "MLflow"
copyright = "MLflow Project, a Series of LF Projects, LLC. All rights reserved"
author = "MLflow"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

import mlflow.version

# The short X.Y version.
version = mlflow.version.VERSION
# The full version, including alpha/beta/rc tags.
release = mlflow.version.VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# We exclude "registry.rst" because it is an orphan redirect
exclude_patterns = ["registry.rst"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_context = {
    "gtm_id": os.environ.get("GTM_ID", ""),
}

html_theme_path = ["../theme/"]
html_theme = "mlflow"
html_favicon = "_static/favicon.ico"


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
# html_title = 'MLflow v0.0.1'

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_js_files = ["runllm.js"]
# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

html_permalinks_icon = " "

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
# Ref: https://sphinx-tabs.readthedocs.io/en/latest/#sphinx-configuration
htmlhelp_basename = "MLflowdoc"

# Disable closing tab for sphinx-tab extension.
sphinx_tabs_disable_tab_closing = True


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "MLflow.tex", "MLflow Documentation", "Databricks", "manual"),
]

# Mock torch & fastai imports as per suggestion in
# https://github.com/sphinx-doc/sphinx/issues/6521#issuecomment-505765893
autodoc_mock_imports = ["torch", "fastai"]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "MLflow", "MLflow Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "MLflow",
        "MLflow Documentation",
        author,
        "MLflow",
        "End-to-end machine learning toolkit.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# Enable nitpicky mode to log warnings for broken references
nitpicky = True
nitpick_ignore = [
    # Ignore a missing reference in `mlflow/store/entities/paged_list.py`
    ("py:class", "T"),
    # Ignore "parent class reference not found" errors for subclasses of ``object``
    ("py:class", "object"),
    ("py:class", "enum.Enum"),
    ("py:class", "bytes"),
    ("py:class", "bytearray"),
    # Suppress warnings for missing references in type annotations
    ("py:class", "dataclasses.dataclass"),
    ("py:class", "numpy.dtype"),
    ("py:class", "numpy.ndarray"),
    ("py:class", "pandas.core.series.Series"),
    ("py:class", "pandas.core.frame.DataFrame"),
    ("py:class", "pandas.DataFrame"),
    ("py:class", "pyspark.sql.DataFrame"),
    ("py:class", "pyspark.sql.dataframe.DataFrame"),
    ("py:class", "matplotlib.figure.Figure"),
    ("py:class", "plotly.graph_objects.Figure"),
    ("py:class", "PIL.Image.Image"),
    ("py:class", "mlflow.deployments.base.BaseDeploymentClient"),
    ("py:class", "Endpoint"),
    ("py:class", "mlflow.types.schema.Array"),
    ("py:class", "mlflow.types.schema.DataType"),
    ("py:class", "mlflow.types.schema.ColSpec"),
    ("py:class", "mlflow.types.schema.TensorSpec"),
    ("py:class", "mlflow.types.schema.Schema"),
    ("py:class", "mlflow.types.schema.Object"),
    ("py:class", "mlflow.types.schema.ParamSchema"),
    ("py:class", "mlflow.types.schema.ParamSpec"),
    ("py:class", "opentelemetry.trace.span.Span"),
    ("py:class", "opentelemetry.trace.status.Status"),
    ("py:class", "opentelemetry.trace.status.StatusCode"),
    ("py:class", "opentelemetry.sdk.trace.ReadableSpan"),
    ("py:class", "mlflow.entities.trace_status.TraceStatus"),
    ("py:class", "ModelSignature"),
    ("py:class", "ModelInputExample"),
    ("py:class", "abc.ABC"),
    ("py:class", "Model"),
    ("py:class", "mlflow.models.model.Model"),
    ("py:class", "mlflow.models.signature.ModelSignature"),
    ("py:class", "mlflow.models.resources.Resource"),
    ("py:class", "mlflow.models.resources.ResourceType"),
    ("py:class", "mlflow.models.dependencies_schemas.set_retriever_schema"),
    ("py:class", "mlflow.metrics.genai.base.EvaluationExample"),
    ("py:class", "mlflow.models.evaluation.base.EvaluationMetric"),
    ("py:class", "MlflowInferableDataset"),
    ("py:class", "csr_matrix"),
    ("py:class", "csc_matrix"),
    ("py:class", "datetime.datetime"),
    ("py:class", "scipy.sparse.csr.csr_matrix"),
    ("py:class", "scipy.sparse.csc.csc_matrix"),
    ("py:class", "scipy.sparse._csr.csr_matrix"),
    ("py:class", "scipy.sparse._csc.csc_matrix"),
    ("py:class", "pathlib.Path"),
    ("py:class", "pydantic.main.BaseModel"),
    ("py:class", "ConfigDict"),
    ("py:class", "FieldInfo"),
    ("py:class", "ComputedFieldInfo"),
    ("py:class", "keras.src.callbacks.callback.Callback"),
    ("py:class", "keras.callbacks.Callback"),
    ("py:class", "keras.src.callbacks.Callback"),
    ("py:class", "pytorch_lightning.callbacks.callback.Callback"),
    ("py:class", "pytorch_lightning.trainer.trainer.Trainer"),
    ("py:class", "pytorch_lightning.core.module.LightningModule"),
    ("py:class", "pytorch_lightning.core.LightningModule"),
    ("py:class", "torch.dtype"),
    ("py:class", "function"),
    ("py:class", "string"),
    ("py:class", "number"),
    ("py:class", "integer"),
    ("py:class", "object"),
    ("py:class", "array"),
    ("py:class", "boolean"),
    ("py:class", "null"),
]


def _get_reference_map():
    """
    Sphinx computes references for type annotations using fully-qualified classnames,
    so references in undocumented modules (even if the referenced object is exposed via
    a different module from the one it's defined in) are considered invalid by Sphinx.

    Example:
    ```
    def start_run(...) -> ActiveRun:
        # ActiveRun is defined in `mlflow/tracking/fluent.py`
        ...
    ```

    For this code, Sphinx tries to create a link for `ActiveRun` using
    `mlflow.tracking.fluent.ActiveRun` as a reference target, but the module
    `mlflow.tracking.fluent` is undocumented, so Sphinx raises this warning:
    `WARNING: py:class reference target not found: mlflow.tracking.fluent.ActiveRun`.
    As a workaround, replace `mlflow.tracking.fluent.ActiveRun` with `mlflow.ActiveRun`.
    """
    ref_map = {
        # < Invalid reference >: < valid reference >
        "mlflow.tracking.fluent.ActiveRun": "mlflow.ActiveRun",
        "mlflow.store.entities.paged_list.PagedList": "mlflow.store.entities.PagedList",
    }

    # Tracking entities
    for entity_name in mlflow.entities.__all__:
        entity_cls = getattr(mlflow.entities, entity_name)
        invalid_ref = entity_cls.__module__ + "." + entity_name
        valid_ref = f"mlflow.entities.{entity_name}"
        ref_map[invalid_ref] = valid_ref

    # Model registry entities
    for entity_name in mlflow.entities.model_registry.__all__:
        entity_cls = getattr(mlflow.entities.model_registry, entity_name)
        invalid_ref = entity_cls.__module__ + "." + entity_name
        valid_ref = f"mlflow.entities.model_registry.{entity_name}"
        ref_map[invalid_ref] = valid_ref

    return ref_map


REFERENCE_MAP = _get_reference_map()


def resolve_missing_references(app, doctree):
    for node in doctree.traverse(condition=pending_xref):
        missing_ref = node.get("reftarget", None)
        if missing_ref is not None and missing_ref in REFERENCE_MAP:
            real_ref = REFERENCE_MAP[missing_ref]
            text_to_render = real_ref.split(".")[-1]
            node["reftarget"] = real_ref
            text_node = next(iter(node.traverse(lambda n: n.tagname == "#text")))
            text_node.parent.replace(text_node, Text(text_to_render, ""))


def setup(app):
    languagesections.setup(app)
    app.connect("doctree-read", resolve_missing_references)


linkcheck_ignore = [
    # Ignore local URLs when validating external links
    r"http://localhost:\d+/?",
]
