# Secfi-assessment
Secfi Backend Assessment

<ul>
    <li><a href="#disclaimer">Disclaimer</a></li>
    <li><a href="#assumptions">Assumptions</a></li>
    <li><a href="#original-design">Original Design</a></li>
    <li><a href="#the-challenge">The Challenge</a></li>
    <li><a href="#run-command">Run Command</a></li>
    <li><a href="#testing-commands">Testing Commands</a></li>
    <li><a href="#next-steps">Next steps</a></li>
    <li><a href="#questions-answers">Questions Answers</a></li>
</ul>

## Assumptions
* The `option_grants` field in the request data has array type while a dictionary makes sense more as it should only be one item so will work with that
* The date send in the request has no specified format so I will assume it has DD-MM-YYYY format
* The price evaluation before first date is the same as first date
* The price evaluation after last date is the same as last date
* The price evaluation between two dates is the same as the price at the first date
## Run Command
Make sure you have `docker` installed on your machine then run:
  ```sh
    make run
  ```