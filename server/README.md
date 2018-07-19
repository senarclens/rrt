# REST Regression Tester (RRT)

Implemented a minimalistic tool to perform regression tests between two
versions of a REST API.

## Proof of Concept
The proof of concept implementation is `rrt.bash`.

### Limitations:
- All changes (also intentional enhancements) are shown as failures.
- It only supports GET
requests.

### Requirements:
`$ sudo -H pip install httpie`
In order to run the included sample API versions, you also need
`sudo -H pip install flask-restful`
The sample APIs can be started via
`cd server`
`python3 v1.py`
`python3 v2.py`

### Usage
1. Fill `requests.csv` with your requests.
2. Adjust the values of $old and $new to the base urls of your rest API.
3. Execute the tests via `rrt.bash`
4. If you'd like to show all performed requests (not just failures),
   add the `-v` parameter
