# DEVELOPER NOTES

## Default environment

Description here!

## Versioning

> We are using [Semantic versioning 2.0.0](http://semver.org/)

Given a version number MAJOR.MINOR.PATCH, increment the:

1. *MAJOR* version when you make incompatible API changes,
2. *MINOR* version when you add functionality in a backwards-compatible
   manner, and
3. *PATCH* version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as
extensions to the MAJOR.MINOR.PATCH format.

## Testing

Unit tests are a prerequisite, which must be implemented independently
for each module individually. Tests in a runtime environment are
implemented via Travis CI. To do this, a successful build must run
within a developer branch.

## Changelog

All changes in the minor area must be listed in the changelog. Bug fixes
on patch level are implemented in a separate branch and will be
documented within the minor version during the next release.
