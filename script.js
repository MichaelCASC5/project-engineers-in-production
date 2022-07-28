const configs = {
	w:800,
	h:700
}

var list = []

class Particle{
    constructor(a,b,c){
        this.x = a
        this.y = b
        this.z = c
    }
    setX(n){
        this.x = n
    }
    setY(n){
        this.y = n
    }
    setZ(n){
        this.z = n
    }
    getX(){
        return this.x
    }
    getY(){
        return this.y
    }
    getZ(){
        return this.z
    }
    draw(){
        let p = 100.0 / this.y
		
		let a = (int)((configs.w/2)+(p*(this.x)))
        let b = (int)(((configs.h/2)-(p*this.z)))

        ellipse(a,b,50*p,50*p)
    }
}

function setup(){
    createCanvas(configs.w,configs.h)
}

function draw(){
    background("black")
	fill("white")
    stroke("black")
	
	if(Math.random() < 1){
		let x_rand = 8000-(int)(Math.random()*16000)
		let y_rand = 500-(int)(Math.random()*1000)
        let z_rand = 8000-(int)(Math.random()*16000)
		
		list.push(new Particle(x_rand,3000,z_rand))
	}
	
	for(let i=0;i<list.length;i++){
		list[i].setY(list[i].getY()-10)
		if(list[i].getY() > 0){
			list[i].draw()
		}else{
			list.splice(i,1)
		}
	}
}