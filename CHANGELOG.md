## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

## [0.7.0] - 2024-04-04

### Added

- Send user newsletter subscription status in the user token

## [0.6.0] - 2024-03-13

### Added

- Set cross domain csrf token on user api get request

## [0.5.0] - 2023-12-07

### Added

- Bind user permissions into the claim of the JWT Token
  (is_active, is_staff, is_superuser)

### Fixed

- Return user information in the User API endpoint even
  if the user is not active

## [0.4.0] - 2022-07-28

### Added

- Bind user preference language into the claim of the JWT Token

## [0.3.0] - 2022-04-07

### Added

- Add a User API endpoint to first generate a JWT for Authentication purpose
  from Third Party Application

### Changed

- Generate JWT Token through Simple JWT's AccessToken class

## [0.2.1] - 2019-10-10

### Fixed

- ACL: Support filenames using `@` and `+` (e.g. course problem responses
  report)
- Fix CI tree creation order

## [0.2.0] - 2019-05-21

### Added

- Add ACL view to control access to instructor dashboard exported files
- Add `cms` and `nginx` services to development environment
- Add a POC using a schema-driven development (using
  `API Blueprint <https://apiblueprint.org/>`\_).


[unreleased]: https://github.com/openfun/fonzie/compare/v0.7.0...master
[0.7.0]: https://github.com/openfun/fonzie/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/openfun/fonzie/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/openfun/fonzie/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/openfun/fonzie/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/openfun/fonzie/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/openfun/fonzie/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/openfun/fonzie/compare/b31adef...v0.2.0
