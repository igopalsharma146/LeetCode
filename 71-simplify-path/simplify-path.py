class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        st = []
        print(components)
        for comp in components:
            if comp == "" or comp == ".":
                continue
            
            if comp == "..":
                if st:
                    st.pop()
            else:
                st.append(comp)
            print(st)
        print(st)
        return "/" + "/".join(st)