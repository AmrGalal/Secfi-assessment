# Secfi-assessment
Secfi Backend Assessment

<ul>
    <li><a href="#assumptions">Assumptions</a></li>
    <li><a href="#run-command">Run Command</a></li>
    <li><a href="#questions-answers">Questions Answers</a></li>
</ul>

## Assumptions
* Constraints on request data field in task A apply to task B as well
* The `option_grants` field in the request data has array type while a dictionary makes sense more as it should only be one item so will work with that
* The date send in the request has no specified format so I will assume it has DD-MM-YYYY format
* The price evaluation before first date is the same as first date
* The price evaluation after last date is the same as last date
* The price evaluation between two dates is the same as the price at the first date

## Run Command
### With Docker
1. Make sure you have `docker` installed on your machine then run:
    ```sh
    make run
    ```
### Manual setup
If you want to run it locally without docker you need to do as follows. <br>
1. Clone the repo
   ```sh
   git clone git@gitlab.com:getocto1/backend/internal-account-service-ias.git
   ```
2. Make sure you have a `pip` and `virtualenv` installed on your machine
    To install:
    ```sh
    sudo apt install python3-pip && pip3 install virtualenv
    ```
3. Create a virtual environment and activate it
   ```sh
    virtualenv venv && source {ABSOLUTE_PATH_TO_VENV}/venv/bin/activate  
   ```

   It's preferable to create the venv outside your workdir as it slows down the file processing of some IDEs.
   However, if it works with you in any other way then that's great.

4.  Install requirements using poetry
    ```sh
    poetry install
    ```
5. Run the server
    ```sh
    python3 manage.py runserver --settings=config.settings
    ```

## Questions Answers
* What are some of the design decisions you made?
    > The task isn't big to have design decisions but I decided to go with Python/Django stack as it's the one am most familiar with.
* What are some of the business decisions you made?
    > The description doesn't show a clear path to follow to calculate the monthly shares for each month. I decided that it has consistent increment every month and it either starts at first month or 13th month depending if we have cliff or not.<br />
    This means that on 13th month, we will always have 25% of shares and 100% of shares by the end of the period.
* How much time did you end up spending on it?
    > About 4-5 hours split onto 2 days to understand the project and start it from scratch
* What do you like about your implementation?
    > I believe it's simple, to the point and easy to understand given that you have context
* What would you improve next time?
    > Add more elaborate tests that test different vesting plans <br />
    > Maybe use a lighter framework such as NodeJS as it's a service that doesn't need alot<br />
* What things are missing to make it production-ready?
    > More people to look at the approach and provide feedback
    > E2E testing and load testing to make sure it behaves as needed
    > Manually make sure all the supported vesting plans work as expected
