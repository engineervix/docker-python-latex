# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.0.1](https://github.com/engineervix/docker-python-latex/compare/v1.0.0...v1.0.1) (2024-07-01)


### 📝 Docs

* update README ([4b0f00c](https://github.com/engineervix/docker-python-latex/commit/4b0f00c8731eb9c2bebc395475e24c5277b9a505))


### 🐛 Bug Fixes

* use correct label and ensure --build-arg is used which each argument ([4a0d310](https://github.com/engineervix/docker-python-latex/commit/4a0d3105bf061b13993d6b306677c833e6402612))

## [v1.0.0](https://github.com/engineervix/docker-python-latex/compare/v0.4.0...v1.0.0) (2024-07-01)


### ⚠ BREAKING CHANGES

* tagging format has changed in order to maintain similarity with official python images

### 👷 CI/CD

* update actions/checkout action to v4 ([#16](https://github.com/engineervix/docker-python-latex/issues/16)) ([be4ed1a](https://github.com/engineervix/docker-python-latex/commit/be4ed1a286b6c23330dfbc6a156918c650dfce8b))
* update actions/setup-node action to v4 ([#17](https://github.com/engineervix/docker-python-latex/issues/17)) ([ab2c2f8](https://github.com/engineervix/docker-python-latex/commit/ab2c2f8280e26e692ae921a005302e6c884359dc))
* update softprops/action-gh-release action to v2 ([#23](https://github.com/engineervix/docker-python-latex/issues/23)) ([d85dea8](https://github.com/engineervix/docker-python-latex/commit/d85dea8adcf56aa5c512fed0028bfb5a7db61c9b))


### ⚙️ Build System

* **deps-dev:** update dependency commitizen to v3.18.1 ([#22](https://github.com/engineervix/docker-python-latex/issues/22)) ([1f1b9dc](https://github.com/engineervix/docker-python-latex/commit/1f1b9dcc80ad7e9da48640a95655f087070d90bd))
* **deps:** update dependency commitizen to v3.14.1 ([#14](https://github.com/engineervix/docker-python-latex/issues/14)) ([8a3dd10](https://github.com/engineervix/docker-python-latex/commit/8a3dd107048fd54faa9c5edfd3c5c84355e133c6))
* **deps:** update node.js to v18.19.1 ([#21](https://github.com/engineervix/docker-python-latex/issues/21)) ([9942450](https://github.com/engineervix/docker-python-latex/commit/994245029083c0f29eb87597b41ea2561f4767c2))
* update node.js to v18.19.0 ([#15](https://github.com/engineervix/docker-python-latex/issues/15)) ([2554df0](https://github.com/engineervix/docker-python-latex/commit/2554df051bebc26435a315c62e80c3d89e87e2bc))


### 🚀 Features

* add Python 3.12 and Debian Bookworm support ([d7122b8](https://github.com/engineervix/docker-python-latex/commit/d7122b86c72eb6335a0b1436e221fbcb98bac3db))

## [v0.4.0](https://github.com/engineervix/docker-python-latex/compare/v0.3.1...v0.4.0) (2024-02-04)


### 🚀 Features

* add multi-arch support ([7254572](https://github.com/engineervix/docker-python-latex/commit/72545721fcff677a1b1a50bf06127fdc80ffa869))

## [v0.3.1](https://github.com/engineervix/docker-python-latex/compare/v0.3.0...v0.3.1) (2023-06-27)


### 👷 CI/CD

* allow for running publishing workflow manually from the Actions tab ([8cb0d4e](https://github.com/engineervix/docker-python-latex/commit/8cb0d4e771e19f6c8ec36f746f914560c8e4ce56))


### 🐛 Bug Fixes

* another attempt to correct the tagging ([3eed45a](https://github.com/engineervix/docker-python-latex/commit/3eed45ac37c4847c96a0e6d8d7cf6ae82c41179a))
* specify project before tagging ([050b6c4](https://github.com/engineervix/docker-python-latex/commit/050b6c44b92ad99f54623917382a12c69adc674c))

## [v0.3.0](https://github.com/engineervix/docker-python-latex/compare/v0.2.0...v0.3.0) (2023-06-26)


### 🚀 Features

* support multiple python versions ([e9aeaad](https://github.com/engineervix/docker-python-latex/commit/e9aeaadef4b4bf75d5a0c1db05b4b94c04de83ed))


### ♻️ Code Refactoring

* add project version management tools ([3860469](https://github.com/engineervix/docker-python-latex/commit/3860469dc48af9e5f8efcb23076fb2de92c1b560))


### ⚙️ Build System

* update .dockerignore ([5a82540](https://github.com/engineervix/docker-python-latex/commit/5a825409f7399126e5d84bb23df78bc47fa995ad))


### 👷 CI/CD

* update docker/build-push-action digest to e27bcee ([#2](https://github.com/engineervix/docker-python-latex/issues/2)) ([238826d](https://github.com/engineervix/docker-python-latex/commit/238826d5f3024073b9ba88bbc9d6fed8a3df9da7))
* update docker/login-action digest to 21f251a ([#3](https://github.com/engineervix/docker-python-latex/issues/3)) ([ebabe71](https://github.com/engineervix/docker-python-latex/commit/ebabe71a1d346e1a4204e378ce02060e9c397b05))
* update docker/metadata-action digest to 59bc9dd ([#5](https://github.com/engineervix/docker-python-latex/issues/5)) ([9c58d5e](https://github.com/engineervix/docker-python-latex/commit/9c58d5e2093b99e6f0a0b3353b7a915f7dd27469))
* update GitHub Actions configs ([cd97aa4](https://github.com/engineervix/docker-python-latex/commit/cd97aa430b5bb0ad9b5984f0f87e6e9804a6395e))


### 📝 Docs

* add badges ([67e7a64](https://github.com/engineervix/docker-python-latex/commit/67e7a64ee5c734669516bb64f5416ed508ebea05))
* update CHANGELOG ([355af6d](https://github.com/engineervix/docker-python-latex/commit/355af6ddd28a46565c8505ffd239bf60e336f623))

## [v0.2.0](https://github.com/engineervix/docker-python-latex/compare/v0.1.0...v0.2.0) (2022-09-19)

### 🚀 Features

* use slim-bullseye instead of bullseye ([3fc4e12](https://github.com/engineervix/docker-python-latex/commit/3fc4e12086bddfd101a1775369d4f3064df24903))

## [v0.1.0](https://github.com/engineervix/docker-python-latex/compare/v0.0.0...v0.1.0) (2023-09-19)

### 🚀 Features

* initial commit ([fe02890](https://github.com/engineervix/docker-python-latex/commit/fe02890074be2d398937d4c989ba13ecca3f8a48))

### 👷 CI/CD

* add docker image publishing workflow ([48baf6d](https://github.com/engineervix/docker-python-latex/commit/48baf6dde2379ef49ac10a8aeec557942266e29c))
* add GitHUb Actions job to Build the Docker image ([3846eea](https://github.com/engineervix/docker-python-latex/commit/3846eeada5aef77cf01c3ef2d4df7daa8f89ffb6))

### ⚙️ Build System

* add .dockerignore and renovate config ([528a06f](https://github.com/engineervix/docker-python-latex/commit/528a06f1daf5b1cd31c65f0cbf2e57de528e8bcb))

### 📝 Docs

* add LICENSE ([6320d86](https://github.com/engineervix/docker-python-latex/commit/6320d869b8baaf9445333cc020e7a77e76d26667))
