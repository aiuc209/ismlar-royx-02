def ismni_aylantir(ism):
    return ", ".join(reversed(ism.split()))

ismlar = ["John Doe", "Jane Smith", "Bob Johnson"]
aylantirilgan_ismlar = [ismni_aylantir(ism) for ism in ismlar]
print(aylantirilgan_ismlar)
