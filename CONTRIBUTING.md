# Dash AG Grid Contributing Guide

Dash AG Grid welcomes community contributions!

If you have identified a bug or have an idea for a new feature, it's best to start with a GitHub issue. First look at existing issues at https://github.com/plotly/dash-ag-grid/issues to make sure this is not a duplicate. Then create a new issue. Bug reports should be accompanied by a small example app that someone else can copy and run to reproduce the problem.

If you have questions, please ask on the [Dash Community Forum](https://community.plotly.com/). rather than using GitHub issues.

### Developing in This Repo

Make sure you have Dash installed with dev and testing extras:

```
pip install dash[dev,testing]
```

Build the component (from the root of this repo):

```
npm i
npm run build
```

Now install the component in development mode:

```
$ pip install -e .
```

In development mode, Python uses the files in this directory when you import the package. So you can write a testing app in another folder, and whenever you change some code and rebuild the component here it will update in your testing app.

#### The Build Process

Dash AG Grid uses [`dash-generate-components`](https://dash.plotly.com/dash-3-for-component-developers) to read the JavaScript file `src/lib/components/AgGrid.react.js` and generate `dash_ag_grid/AgGrid.py` (along with similar files for R and Julia). `AgGrid.py` only changes when the React component's interface changes, so do not be surprised if internal changes to `AgGrid.react.js` do not result in changes to `AgGrid.py`.

### Versioning

We follow a strict versioning system aligned with the underlying Ag Grid version, but also reserving the
patch number for updates to the Dash grid.

Specifically, Dash Ag Grid will always have the same _major_ and _minor_ version number as the Javascript Ag Grid package it is bundling, but it may not always have the same patch number.

Ag Grid releases new major versions every 6-8 months, and minor versions every 4-6 weeks. Sometimes, Dash Ag Grid may introduce new changes that warrant a minor release according to [semver](https://semver.org/): For example, exposing a functional property of Ag Grid as a declarative property in Dash Ag Grid. In this case, we would wait for a new minor release of Ag Grid and bump the versions together.

We may release out-of-band of Ag Grid when there are patches that we want to make available.

As a user, you can always check the underlying Ag Grid version with `dash_ag_grid.grid_version` and the underlying Dash Ag Grid version with `dash_ag_grid.__version__`.

For maintainers, when issuing new releases ensure that the version bump of Dash Ag Grid follows this convention. This can be verified after a build by using `npm run pre-flight-dag-version` or `python test_versioning.py`. This is validated during the `npm run dist`

### Create a Production Build

Update the package version in `package.json` and `CHANGELOG.md` and ensure the changelog lists all the important updates. Then reinstall (so `package-lock.json` gets the new version) and rebuild:

```
npm i
npm run build
```

Commit this - either via a PR or directly to the main branch. Then you can create source and wheel distributions in the generated `dist/` folder, after emptying out any previous builds:

```
npm run dist
```

### Publish a New Release

A Github release with package build files is automatically generated when a new tag starting with `v*` is pushed.

Once a Github release is published, the build is re-generated and pushed to PyPi.

Create a git tag:

```
git tag -a 'v31.0,1' -m 'v31.0.1'
git push --tags
```

Wait for the "Generate release" CI job to complete, then check the releases tab to move the release from "Draft" to "Published". Make sure to copy in the Changelog.

When the release is published to Github, it's automatically pushed to PyPi as well.

Finally, announce the release in Slack, in both the `#dash-product` and `#community-ag-grid` channels. You're done!
