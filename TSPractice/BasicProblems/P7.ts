// Program to Display All Prime Numbers from 1 to N

function findAllPrime(a : number) : void {
    let x : number;
    let y : number;
    let flag : number;
    for (x = 1; x <= a; x++) {
        if(x === 0 || x === 1) {
            console.log("Given Number is a prime number");
            continue;
        }
        flag = 1;
        for(y = 2; y <= x/2; y++) {
            if(x%y === 0) {
                flag = 0;
                break;
            }
        }
        if(flag === 1) {
            console.log(x);
        }
    }
}

findAllPrime(1);
