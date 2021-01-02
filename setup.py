import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdocs_material_multilang_toc",
    version="0.0.1",
    author="JustBeYou",
    author_email="mihailferaru2000@gmail.com",
    description="Multilanguage ToC for mkdocs-material",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_material_multilang_toc = mkdocs_material_multilang_toc.__init__:Plugin',
        ]
    }
)
