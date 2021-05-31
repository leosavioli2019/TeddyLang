<main>
    !(href="/") Voltar !
    %
        <teddy>
            
            count = int(str(GET("first")))
            while count != 1 do
                TPRINT(f"--{count}--")
                if count % 2 == 0 do
                    count = count // 2
                else
                    count = count * 3 + 1
                end
            end
            TPRINT("--1--")
        </teddy>
    %
</main>