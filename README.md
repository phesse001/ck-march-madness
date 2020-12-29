# Collective Knowledge workflows for MarchMadness




# Notes

Pull CK repo

```
ck pull repo --url=<repo url>
```

List programs

```
ck ls program
```

List all datasets
```
ck ls dataset
```

List compatible datasets
```
ck search dataset --tags=march-madness
```

Compile the program once

```
ck compile program:simulator
```

Run the program once
```
ck run program:simulator
```

Run the program multiple times as a part of a proper experiment:
```
ck benchmark program:simulator --repeititions=10
```

Run the program while changing some run-time parameters:
```
ck run program:simulator --env.apply_scaling_1=100
```
 or
```
ck benchmark program:simulator --env.apply_scaling_1=100
```
Run compiler autotuning experiment
```
ck autotune program:simulator --iterations=100 --repetitions=4 --record_uoa=march-madness-experiment --gcc
```
See results
```
ck plot graph:<experiment uoa>
```
or
```
ck browse experiment:<experiment uoa>
```
Replay a specific point
```
ck replay experiment:<experiment uoa> --point=<point uoa>
```



Related repositories:
* https://github.com/ctuning/ck-scc18
* https://github.com/ctuning/ck-scc
