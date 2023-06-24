# Conway's Game of Life

This is my python implementation of CGOL. The Gameboard can be any size as long as it's square. You can load different initial configurations by editing the board variable in the main function.

![Edit this variable](/media/edit.png)

<br>

⚠️ After starting the program, press Enter to start ⚠️

<br>
<br>

## Requirements
You will need to download these libraries:

<code>colorama</code>
<code>keyboard</code>

## Patterns
I implemented a few well-known initial patterns which are stored in the initials.py file. By the time of writing this, the following patterns are added:

### 1. Blinker

Type: _Oscillator_ \
Period: _2_

```py
board = blinker()
```

![blinker](/media/blinker.gif)



<br>



### 2. Toad

Type: _Oscillator_ \
Period: _2_

```py
board = toad()
```

![blinker](/media/toad.gif)



<br>



### 3. Beacon

Type: _Oscillator_ \
Period: _2_

```py
board = beacon()
```

![blinker](/media/beacon.gif)



<br>



### 4. Pulsar

Type: _Oscillator_ \
Period: _3_
```py
board = pulsar()
```

![blinker](/media/pulsar.gif)



<br>



### 5. Pentadecathlon

Type: _Oscillator_ \
Period: _15_

```py
board = pentadecathlon()
```

![blinker](/media/penta.gif)



<br>



### 6. glider

Type: _Spaceship_

```py
board = glider()
```

![blinker](/media/glider.gif)



<br>



### 7. Light-weight Spaceship

Type: _Spaceship_

```py
board = LWSS()
```

![blinker](/media/lwss.gif)



<br>



### 8. Medium-weight Spaceship

Type: _Spaceship_

```py
board = MWSS()
```

![blinker](/media/mwss.gif)



<br>



### 9. Heavy-weight Spaceship

Type: _Spaceship_

```py
board = HWSS()
```

![blinker](/media/hwss.gif)



<br>



### 10. Custom

To make your own initial pattern just edit the custom function at the bottom of the <code>initials.py</code> file
```py
board = custom()
```

![custom](/media/custom.png)
