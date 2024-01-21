===============
contents
===============

* `Packaging`_

Packaging
=========

`package book <https://r-pkgs.org/>`_

`pkg website <https://pkgdown.r-lib.org/>`_

`cran note <https://cran.r-project.org/doc/manuals/R-exts.html#Creating-R-packages>`_

`pkg tute <http://web.mit.edu/insong/www/pdf/rpackage_instructions.pdf>`_

Quick Example
-------------

Set up:

.. code-block:: r

    library(devtools)
    create_package("C:\\Users\\yzdom\\Projects\\regexcite")
    # edit DESCRIPTION

    # advanced
    use_git()
    use_mit_license()
    use_testthat()
    use_readme_rmd()

Contents:

.. code-block:: r

    # add function
    use_package("stringr")
    use_r("strsplit1")
    # rename_files("strsplit1", "str_split_one")

    # spot checks
    # load_all() -> spot check -> edit -> ...
    load_all()

    # tests
    use_test("strsplit1")
    # edit tests and code -> test() -> ...
    test()

    # doco
    # add Roxygen comments -> document() -> ?fn -> ...
    document()

    # readme
    # edit README.Rmd -> build_readme() -> inspect -> ...
    build_readme()

publish:

.. code-block:: r

    check()
    install()
    # push
