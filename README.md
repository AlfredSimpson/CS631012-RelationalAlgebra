# CS631012-RelationalAlgebra
 
This was designed for use in a database course at NJIT.

During this course, we are instructed to use the [RelaX](https://dbis-uibk.github.io/relax/) tool to write relational algebra expressions. This tool is great for learning, but it comes with a learning curve of its own. This repository was designed to help students (like me) use RelaX more effectively.

## How to use this tool:

1. Clone this repository to your local machine.
2. Open the repo in bash or powershell (command prompt may work, but it will not colorize your text).
3. Run the python file from the root of the repository. I used this command, but yours may be different:
```bash
py ./BuildRelations/BuildRelations.py
```
4. From here, the python program will prompt you to begin building your relation. As of the time of writing, this program was designed specifically for the first homework. It will prompt you for the required relation names, all with prebuilt attributes. If you need to add more attributes, you will need to modify the python file. I may add this functionality in the future.
5. Once you have built your raw-relations, run command 5 to generate the working relation files to be used in RelaX. These files will be placed in the `./Relations` directory.
6. If you wish to upload them to RelaX as a dataset, run command 6. This will then move all of the ./Relations files to their own subdirectory in the Relations directory. it will also create a dataset in BuiltDatasets. You can then upload this to RelaX.