import setuptools

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "ubuntu-llmops"
AUTHOR_USER_NAME = "louayamor"
PACKAGE_NAME = "ubuntu_llmops"
AUTHOR_EMAIL = "amor.louay20@gmail.com"

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="LLM-powered Ubuntu system reporting and reasoning platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.11,<3.13",
    install_requires=[
        "langchain",
        "langchain-community",
        "langgraph",
        "crewai",
        "aiohttp",
        "python-dotenv",
        "pandas",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Monitoring",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
