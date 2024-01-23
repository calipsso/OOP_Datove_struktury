class Convert:
    @staticmethod
    def imperial(a, b):
        return a * b

    @staticmethod
    def metric(a, b):
        return a/b

print(f" Convert to Imperial {Convert.imperial(5, 1.0936)}")
print(f" Convert to Metric {Convert.metric(5, 1.0936)}")

