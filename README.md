# devagent-review-smoke

Minimal repository used to exercise DevAgent's GitHub pull-request review flow.

The `main` branch contains a safe download path resolver. Test pull requests can
introduce a small, reviewable regression without depending on application
infrastructure.

Each smoke update stays intentionally small so review comments can be traced to
one pull-request snapshot.
