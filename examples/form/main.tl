<main>
    <include>"calc": {"method": ["GET"], "file": "calc.tl"}</include>
    #DIGITE UM NÚMERO#
    {[]}(action="/calc", method="GET")
        ???(type="number" name="first")???
        ???(type="submit" name="submit")???
    {[]}
</main>