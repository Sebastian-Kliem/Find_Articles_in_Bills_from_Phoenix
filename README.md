# Read bills from dealer Phoenix

This app reads bills in PDF-format from the dealer Phoenix and search in it for given article number.

It returns the billing-numbers and date.

## Installing

Download the full directory

Install requirements:

    pip install -r requirements.txt


## Usage

Make sure, you put the bills in directory "Bills"

On commandline:
    
    ./findArticlenumber.py <articlenumber>

or

    python3 ./findArticlenumber.py <articlenumber>

## License

    The code in this repository is licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

**NOTE**: This software depends on other packages that may be licensed under different open source licenses.