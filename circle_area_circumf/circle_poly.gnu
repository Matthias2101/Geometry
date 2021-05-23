
#runden Kreis erzeugen
set size ratio -1

set polar

#erst set polar dann unset, sonst wird r axe neu gesetzt
unset key; unset tics; unset border
unset raxis

set style line 1 lc rgb '#0060ad' lt 1 lw 2     # --- blue
set style line 2 lc rgb '#dd181f' lt 1 lw 2     # --- red
set style line 3 lc rgb "green" lt 1 lw 2     # --- gruen
set style line 4 lc rgb "black" lt 1 lw 1     # --- gruen

set lmargin 0
set rmargin 1
set tmargin 1
set bmargin 0


set xrange [-2:2]
set yrange [-2:2]
set trange [0:2*pi]

set samples 500

n = 20

x0 = cos(0)
y0 = sin(0)

ra = 1/cos(2*pi/(2*n))

xa0 = ra * cos(0)
ya0 = ra * sin(0)

do for [k=1:n] {
	phi = k *(2*pi/n)
	x1 = cos(phi)
	y1 = sin(phi)

	xa1 = ra * cos(phi)
	ya1 = ra * sin(phi)
	set arrow from 0,0 to x1,y1 nohead ls 4 front
	set arrow from 0,0 to xa1,ya1 nohead ls 4 front 
	set arrow from x0,y0 to x1,y1 nohead ls 4 front
	set arrow from xa0,ya0 to xa1,ya1 nohead ls 4 front
	x0 = x1
	y0 = y1
 
	xa0 = xa1
	ya0 = ya1
}

f(t)=1

#draw circle
plot [0:2*pi] f(t) ls 1
