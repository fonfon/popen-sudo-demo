Demonstration how the `env` parameter of `subprocess.Popen` has no effect when
using sudo.

`foo/run.py` executes `foo/runme` with a changed PYTHONPATH so that
`foo/runme` is able to import from `bar`.

Run it with:

    cd foo
    python3 run.py

Example output:

    $ python3 run.py

    Executing ['/home/fonfon/code/popen/foo/runme']:
    Path of barfile.py: /home/fonfon/code/popen/bar/barfile.py

    Executing ['sudo', '-E', '/home/fonfon/code/popen/foo/runme']:
    Path of barfile.py: ImportError

