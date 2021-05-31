<main>

# Class #

    <teddy>
        class Add do

            def __init__(self, expr) do
                self.expr = expr
            end

            def exprs(self) do
                return eval(self.expr)
            end

        end
        a = Add("1+1")
        TPRINT(f"## {a.exprs()} ##")
    </teddy>
    

</main>