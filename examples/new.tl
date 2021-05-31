<main>

    # Portuguese #

    <teddy>
        
        class Text do

            def __init__(self, textos, contexto) do
                self.textos = textos
                self.contexto = contexto
            end

            def mostrarTítulo(self) do
                TPRINT(f"## {self.contexto} ##")
            end

            def mostrarLista(self) do
                for c in range(0,len(self.textos)) do
                    TPRINT(f"--{self.textos[c]}--")
                end
            end
        end

        setGlobal('text', Text, 'class')
        a = Text(["oi", "olá", "bom dia"], "Saudações")
        a.mostrarTítulo()
        a.mostrarLista()

    </teddy>

    # English #
    
    <teddy>
        Text = getGlobal('text')
        b = Text(["hi","hello","good morning"], "Saudações")
        b.mostrarTítulo()
        b.mostrarLista()
    </teddy>

</main>