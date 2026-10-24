import numpy as np
class DataAnalytics:
    def __init__(self):
        self.arr = None
    # =========================
    # 1. ARRAY CREATION
    # =========================
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        ch = input("Enter your choice: ")
        try:
            if ch == '1':
                n = int(input("Enter number of elements: "))
                shape = (n,)
            elif ch == '2':
                r = int(input("Enter number of rows: "))
                c = int(input("Enter number of columns: "))
                shape = (r, c)
            elif ch == '3':
                d = int(input("Enter depth: "))
                r = int(input("Enter number of rows: "))
                c = int(input("Enter number of columns: "))
                shape = (d, r, c)
            else:
                print("Invalid choice!")
                return
            if any(x <= 0 for x in shape):
                print("Dimensions must be positive!")
                return
            total = int(np.prod(shape))
            data = list(map(int, input(
                f"Enter {total} elements separated by space: "
            ).split()))
            if len(data) != total:
                print("Invalid number of elements!")
                return
            self.arr = np.array(data).reshape(shape)
            print("\nArray created successfully:")
            print(self.arr)
            self.index_slicing()
        except ValueError:
            print("Please enter valid integers!")
    # =========================
    # INDEXING AND SLICING
    # =========================
    def index_slicing(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            ch = input("Enter your choice: ")
            if ch == '1':
                try:
                    print("\nOriginal Array:")
                    print(self.arr)
                    if self.arr.ndim == 1:
                        i = int(input("Enter index: "))
                        result = self.arr[i]
                    elif self.arr.ndim == 2:
                        r = int(input("Enter row index: "))
                        c = int(input("Enter column index: "))
                        result = self.arr[r, c]
                    elif self.arr.ndim == 3:
                        d = int(input("Enter depth index: "))
                        r = int(input("Enter row index: "))
                        c = int(input("Enter column index: "))
                        result = self.arr[d, r, c]
                    print("\nIndexed Element:")
                    print(result)
                except (ValueError, IndexError):
                    print("Invalid Index!")
            elif ch == '2':
                try:
                    ranges = []
                    names = {
                        1: ["element"],
                        2: ["row", "column"],
                        3: ["depth", "row", "column"]
                    }
                    for name in names[self.arr.ndim]:
                        s = input(
                            f"Enter {name} range (start:end): "
                        )
                        start, end = map(int, s.split(":"))
                        ranges.append(slice(start, end))
                    print("\nSliced Array:")
                    print(self.arr[tuple(ranges)])
                except ValueError:
                    print("Invalid range! Use start:end.")
            elif ch == '3':
                break
            else:
                print("Invalid choice!")
    # =========================
    # 2. MATHEMATICAL OPERATIONS
    # =========================
    def maths(self):
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        ch = input("Enter your choice: ")
        if ch not in ['1', '2', '3', '4']:
            print("Invalid choice!")
            return
        try:
            data = list(map(int, input(
                f"Enter {self.arr.size} elements for second array: "
            ).split()))
            if len(data) != self.arr.size:
                print("Invalid number of elements!")
                return
            arr2 = np.array(data).reshape(self.arr.shape)
            print("\nOriginal Array:")
            print(self.arr)
            print("\nSecond Array:")
            print(arr2)
            if ch == '1':
                print("\nAddition:")
                print(self.arr + arr2)
            elif ch == '2':
                print("\nSubtraction:")
                print(self.arr - arr2)
            elif ch == '3':
                print("\nMultiplication:")
                print(self.arr * arr2)
            elif ch == '4':
                if np.any(arr2 == 0):
                    print("Cannot divide by zero!")
                else:
                    print("\nDivision:")
                    print(self.arr / arr2)
        except ValueError:
            print("Invalid input!")
    # =========================
    # 3. COMBINE OR SPLIT ARRAYS
    # =========================
    def combine_split(self):
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        ch = input("Enter your choice: ")
        if ch == '1':
            try:
                data = list(map(int, input(
                    f"Enter {self.arr.size} elements for second array: "
                ).split()))
                if len(data) != self.arr.size:
                    print("Invalid number of elements!")
                    return
                arr2 = np.array(data).reshape(self.arr.shape)
                print("\nOriginal Array:")
                print(self.arr)
                print("\nSecond Array:")
                print(arr2)
                print("\nCombined Array:")
                print(np.vstack((self.arr, arr2)))
            except ValueError:
                print("Invalid input!")
        elif ch == '2':
            try:
                n = int(input("Enter number of parts: "))
                if n <= 0:
                    print("Enter a positive number!")
                    return
                result = np.array_split(self.arr, n, axis=0)
                print("\nOriginal Array:")
                print(self.arr)
                print("\nSplit Arrays:")
                for i, part in enumerate(result, 1):
                    print(f"\nPart {i}:")
                    print(part)
            except ValueError:
                print("Invalid input!")
        else:
            print("Invalid choice!")
    # =========================
    # 4. SEARCH, SORT AND FILTER
    # =========================
    def search_sort_filter(self):
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        ch = input("Enter your choice: ")
        if ch == '1':
            try:
                value = int(input("Enter value to search: "))
                result = np.where(self.arr == value)
                print("\nOriginal Array:")
                print(self.arr)
                if result[0].size > 0:
                    print("\nValue found at indices:")
                    print(result)
                else:
                    print("Value not found!")
            except ValueError:
                print("Invalid input!")
        elif ch == '2':
            print("\nChoose Sorting Order:")
            print("1. Ascending Order")
            print("2. Descending Order")
            order = input("Enter your choice: ")
            print("\nOriginal Array:")
            print(self.arr)
            if order == '1':
                print("\nAscending Order:")
                print(np.sort(self.arr, axis=-1))
            elif order == '2':
                print("\nDescending Order:")
                print(np.flip(np.sort(self.arr, axis=-1), axis=-1))
            else:
                print("Invalid choice!")
        elif ch == '3':
            print("\nChoose a filter:")
            print("1. Greater than")
            print("2. Less than")
            print("3. Equal to")
            op = input("Enter your choice: ")
            if op not in ['1', '2', '3']:
                print("Invalid choice!")
                return
            try:
                value = int(input("Enter value: "))
                if op == '1':
                    result = self.arr[self.arr > value]
                elif op == '2':
                    result = self.arr[self.arr < value]
                else:
                    result = self.arr[self.arr == value]
                print("\nOriginal Array:")
                print(self.arr)
                print("\nFiltered Array:")
                print(result)
            except ValueError:
                print("Invalid input!")
        else:
            print("Invalid choice!")
    # =========================
    # 5. AGGREGATES AND STATISTICS
    # =========================
    def statistics(self):
        print("\nAggregates and Statistics:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        ch = input("Enter your choice: ")
        print("\nOriginal Array:")
        print(self.arr)
        if ch == '1':
            print("\nSum:", np.sum(self.arr))
        elif ch == '2':
            print("\nMean:", np.mean(self.arr))
        elif ch == '3':
            print("\nMedian:", np.median(self.arr))
        elif ch == '4':
            print("\nStandard Deviation:", np.std(self.arr))
        elif ch == '5':
            print("\nVariance:", np.var(self.arr))
        else:
            print("Invalid choice!")
    # =========================
    # MAIN MENU
    # =========================
    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print("Welcome to the NumPy Analyzer!")
            print("=" * 40)
            print("Choose an option:")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            ch = input("Enter your choice: ")
            if ch == '6':
                print("\nThank you for using NumPy Analyzer!")
                break
            if ch in ['2', '3', '4', '5'] and self.arr is None:
                print("\nPlease create an array first!")
                continue
            if ch == '1':
                self.create_array()
            elif ch == '2':
                self.maths()
            elif ch == '3':
                self.combine_split()
            elif ch == '4':
                self.search_sort_filter()
            elif ch == '5':
                self.statistics()
            else:
                print("Invalid choice!")
# =========================
# MAIN PROGRAM EXECUTION
# =========================
if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.menu()