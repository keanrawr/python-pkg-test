# Test Python Package

I'm tired of maintaining a bunch of custom functions for every project I start, in the R community there's a very sensible saying:

> If you repeat a code block 3 times, you need a function. If you repeat a function 3 times, you need a package.

I feel I'm pretty good following the first part of the saying, however, I've written the same function well over 3 times.

I've never been confortable with the idea of creating packages, so I'll channel my Mexica forefathers' spirits to start simple and build on top of it.

## How it's built

I'll be using poetry, since it's the one dependency manager that I'm most familiar with, it's also a great thing that it can handle building an publishing.

To build the project do:

```sh
poetry build
```

## Development milestones

This is a very informal project, so here are some milestiones off the top of my head.

- [ ] Build a hello world package
- [ ] Create tests for the code
- [ ] Add github actions to run tests and build
- [ ] Publish to aws _codeArtifact_, using github actions
- [ ] Add github action to scan code for vulnerabilities
- [ ] Add github action to tag release versions
- [ ] Add some real functions, like a small optimization class
