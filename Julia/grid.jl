function line1(n)
    for k in range(1,stop=n)
        if k==n
            print("+ - - - - +\n")
        else
            print("+ - - - - ")
        end
    end
end

function line2(n,m)
    for i in range(1,stop=m)
        for k in range(1,stop=n)
            if k==n
                print("|         |\n")    
            else
                print("|         ")    
            end
        end
    end
end


function grid(n)
    for k in range(1,stop=n)
        if(k==n)
            line1(n)
            line2(n,4)
            line1(n)
        else
            line1(n)
            line2(n,4)
        end
    end
end

grid(6)