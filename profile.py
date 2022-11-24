# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Emulab specific extensions.
import geni.rspec.emulab as emulab
# for tour, instructions
import geni.rspec.igext as ig


# Create a portal context, needed to defined parameters
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Pick your OS.
imageList = [
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD', 'UBUNTU 20.04'),
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS8S-64-STD',  'CENTOS 8 Stream')]

pc.defineParameter("osImage", "Select OS image",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList,
                   longDescription="Select a disk image.")

#    'c240g5', 'c240g5',  # 32 at Wisconsin
#    'c4130', 'c4130',    # 2 at Wisconsin, 2 at Clemson
#    'r7525', 'r7525'     # 15 at Clemson



# Optional physical type for all nodes.
pc.defineParameter("phystype",  "Physical node type",
                   portal.ParameterType.STRING, "",
                   longDescription="Specify a physical node type (c240g5, c4130, r7525) " +
                   "instead of letting the resource mapper choose for you.")

# Optional ephemeral blockstore
pc.defineParameter("tempFileSystemSize", "Temporary Filesystem Size",
                   portal.ParameterType.INTEGER, 0,advanced=True,
                   longDescription="The size in GB of a temporary file system to mount on each of your " +
                   "nodes. Temporary means that they are deleted when your experiment is terminated. " +
                   "The images provided by the system have small root partitions, so use this option " +
                   "if you expect you will need more space to build your software packages or store " +
                   "temporary files.")
                   
# Instead of a size, ask for all available space. 
pc.defineParameter("tempFileSystemMax",  "Temp Filesystem Max Space",
                    portal.ParameterType.BOOLEAN, True,
                    advanced=True,
                    longDescription="Instead of specifying a size for your temporary filesystem, " +
                    "check this box to allocate all available disk space. Leave the size above as zero.")

pc.defineParameter("tempFileSystemMount", "Temporary Filesystem Mount Point",
                   portal.ParameterType.STRING,"/data",advanced=True,
                   longDescription="Mount the temporary file system at this mount point; in general you " +
                   "you do not need to change this, but we provide the option just in case your software " +
                   "is finicky.")

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Check parameter validity.
if params.tempFileSystemSize < 0 or params.tempFileSystemSize > 200:
    pc.reportError(portal.ParameterError("Please specify a size greater then zero and " +
                                         "less then 200GB", ["nodeCount"]))

pc.verifyParameters()

ubuntuInstructions = """

After the automated install process is complete (you should see a check mark in the corner of the node), open a shell and run:

```
python3-m pip install --user Cython==0.29.32
python3 -m pip install --user -r /local/repository/requirements_cloudlab_dl.txt --extra-index-url https://download.pytorch.org/whl/cu113 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
"""

tourDescription = """
This experiment is for connecting Google Colab to a server running on NSF-supported cloud computing infrastructure.

This allows you to run experiments requiring bare metal access, storage, memory, GPU and compute that exceeds the abilities of Colab's hosted runtime, but with Colab's familiar interface (and notebooks stored in your Google Drive). It also allows you to easily go back and forth between the convenience of Colab's hosted runtime and Chameleon or CloudLab's greater capabilities, as you develop your experiment.
"""

node = request.RawPC('colab')
node.disk_image = params.osImage

# Optional hardware type.
if params.phystype != "":
  node.hardware_type = params.phystype

# Optional Blockstore
if params.tempFileSystemSize > 0 or params.tempFileSystemMax:
    bs = node.Blockstore("colab-bs", params.tempFileSystemMount)
    if params.tempFileSystemMax:
        bs.size = "0GB"
    else:
      bs.size = str(params.tempFileSystemSize) + "GB"
    bs.placement = "any"

if params.osImage[1]=='UBUNTU 20.04':
    node.addService(pg.Execute(shell="bash", command="/local/repository/cloudlab-ubuntu-install.sh"))
    tourInstructions = ubuntuInstructions


tour = ig.Tour()
tour.Description(ig.Tour.TEXT,tourDescription)
tour.Instructions(ig.Tour.MARKDOWN,tourInstructions)
pg.addTour(tour)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
