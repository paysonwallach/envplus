<div align="center">
  <h1>Venn</h1>
  <img width=400px src=https://raw.githubusercontent.com/paysonwallach/venn/master/resources/venn.png>
  <br>
  <p>Mix and match virtual environments</p>
  <a href=https://github.com/paysonwallach/venn/release/latest>
    <img src=https://img.shields.io/badge/release-v0.4.0-blue?style=flat-square>
  </a>
  <a href=https://github.com/paysonwallach/venn/blob/master/LICENSE>
    <img src=https://img.shields.io/badge/license-HIP-994444?style=flat-square>
  </a>
  <a href=https://buymeacoffee.com/paysonwallach>
    <img src=https://img.shields.io/badge/donate-Buy%20me%20a%20coffe-yellow?style=flat-square>
  </a>
  <br>
  <br>
  <br>
</div>

Venn lets you work in multiple [virtual environments](http://www.virtualenv.org/en/latest/virtualenv.html) simultaneously with ease.

A fork of [envplus](https://github.com/tpict/envplus).

## Installation

### Via a Package Manager (Preferred)

#### [Homebrew](https://brew.sh)

Tap the [homebrew-venn](https://github.com/paysonwallach/homebrew-venn) repository:

```sh
brew tap paysonwallach/venn
```

Then install via `brew`:

```sh
brew install venn
```

### From source using [Poetry](https://github.com/sdispater/poetry)

__Note:__ It is recommended to build `venn` in a virtual environment due to dependency version requirements.

From the root of the repository, install the necessary dependencies via `poetry`:

```sh
poetry install
```

Then build the project:

```sh
poetry build
```

Finally, outside of your virtual environment, install using `pip`:

```sh
pip install dist/venn-<version>.tar.gz
```

## How It Works

`venn` takes advantage of Python's [.pth file convention](https://docs.python.org/3/library/site.html). It creates (and manipulates) a special file, `_venn.pth`, in the `site-packages` directory of your current virtualenv.

## Walkthrough

Many data science-related workflows involve fetching and parsing web pages, so let's build a virtual environment that contains a handy trio of packages for this task.

```sh
mkvirtualenv scraping
pip install requests
pip install lxml
pip install cssselect
```

For a lot of projects, you'll probably also want to store information in some sort of database. Let's make a bare-bones virtualenv for this task, too.

```sh
mkvirtualenv dbstorage
pip install dataset
```

Now let's say you're working on a project to scrape cat GIFs from BuzzFeed and store them in a database. Rather than reinstall all the packages above, you can just do this:

```sh
mkvirtualenv buzzcats
venn add scraping dbstorage
```

Now you can use `requests`, `lxml`, `cssselect`, and `dataset` in your `buzzcats` virtualenv. The actions you take in the `buzzcats` virtualenv will not harm or alter your other virtualenvs. (Even if you run `pip uninstall`.) And upgrades to `scraping` and other `venn add`'ed virtualenvs will become immediately available to `buzzcats`.


## Usage

To use `venn`, [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/) must be installed and __your target virtual environment must be currenlty activated__.

---

### venn add [envs]

Make another virtualenv's packages available to your current virtualenv. Accepts multiple, space-separated virtualenv names.

```sh
venn add scraping dbstorage
```

---

### venn remove [envs]

Remove a previously added virtualenv from your current virtualenv. Accepts multiple, space-separated virtualenv names.

```sh
venn remove scraping dbstorage
```

---

### venn pause [envs]

"Pauses" previously added virtualenvs, so that they remain in `_venn.pth` (as commented lines) but do not effect the current virtualenv. If virtualenv names are provided, only those are paused. Otherwise, all previously added virtualenvs are paused.

```sh
# to pause all
venn pause
# to pause just one
venn pause dbstorage
```

---

### venn resume [envs]

Un-pauses previously added virtualenvs. If virtualenv names are provided, only those are resumed. Otherwise, all previously added virtualenvs are resumed.

```sh
# to resume all
venn resume
# to resume just one
venn resume dbstorage
```

---

### venn list [-p] [-a]

List added virtualenvs. By default, lists only *non-paused* additions. `-p` will list only *paused* additions, and `-a` will list *all* additions.

---

### venn run [command]

Temporarily adds your virtualenvs' `bin`-paths to your current `PATH` before running `command`. Lets you use other virtualenvs' command-line programs.

```sh
# create a dummy virtualenv with csvkit
mkvirtualenv csvtest
pip install csvkit

# create newenv and add csvtest
mkvirtualenv newenv
venn add csvtest

# while in newenv, run csvkit's csvcut command-line utility
echo "a,b,c" | venn run csvcut -c 2
```

---

### venn path

Print the path of the active virtualenv's `_venn.pth` file.

```sh
venn path
```

---

### venn describe

Print the contents of the active virtualenv's `_venn.pth` file.

```sh
venn describe
```

---

### venn edit

Open the active virtualenv's `_venn.pth` file in your default editor. You probably shouldn't do this. Mostly for debugging purposes.

```sh
venn edit
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Code of Conduct

By participating in this project, you agree to abide by the terms of the [Code of Conduct](https://github.com/paysonwallach/venn/blob/master/CODE_OF_CONDUCT.md).

## License

[Venn](https://github.com/paysonwallach/venn) is licensed under the [Hippocratic License](https://github.com/paysonwallach/venn/blob/master/LICENSE).
