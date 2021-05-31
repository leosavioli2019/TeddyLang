<main>
    <teddy>
        for c in range(0, int(GET("number"))) do
            if c % 2 == 0 do
                TPRINT(f'--{c} é par--')
            else
                TPRINT(f'--{c} é impar--')
            end
        end
    </teddy>
</main>