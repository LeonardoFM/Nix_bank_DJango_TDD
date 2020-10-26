# Nix_bank_DJango_TDD

This is an API which provide bank functions as create an account, debit and credit transactions. With an account id, the user can call this methods and the extract request shows all of its account interactions.

## Before clonning

The good practices recommend the virtual environment usage as *venv*.

    python -m venv venv

Then we run in Linux OS

    source venv/bin/activate

## Requirements

 - with **python3**
 - all the others just 

<pre><code>pip install -r requirements.txt</code></pre>

 - the API use django so the basic commands to run inside directory project are

<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
<pre><code>python manage.py runserver</code></pre>

## Tests

All tests were written using pytest to cover more then 90% of the API functions.

Inside the project directory we can run the automated tests with the command

    py.test

As we see in *pytest.ini* the covering logs is created inside *htmlcov* folder.