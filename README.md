# DemoService
demo service for the ConnectAPI marketplace


### Install
```shell script
$> git clone https://github.com/ConnectAPI/DemoService.git
$> cd DemoService
$> pip install -r requirements.txt
```

### Run
```shell script
$> cd src
$> python3 run.py
```

### Test
```shell script
$> pip install -r requirements-dev.txt
$> pytest
```

### Routes
- math
  - sum (/math/sum) returns the sum of A and B
  - mul (/math/mul) returns the product of A and B
- random
  - range (/random/range) returns random number between A and B
  - secure (/random/secure) returns random string with length N
