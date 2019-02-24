############################################################
# Image Identifcation (Machine Learning) with Pytorch      #
# Coded by Alisa Khieu                                     #
#                                                          #
# Image Dataset from CIFAR10 with 5000 images of 32x32     #
# Neural network with three layers for classification      #
############################################################

def split_sets():
    '''
    Imports image dataset.
    Splits into training and test sets.
    '''
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True)
    trainset = [(np.asarray(image) / 256, label) for image, label in trainset]
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4096, shuffle=True)

    val_and_test_set = torchvision.datasets.CIFAR10(root='./data', train=False, download=True)
    val_and_test_set = [(np.asarray(image) / 256, label) for image, label in val_and_test_set]

    valset = val_and_test_set[:5000]
    valset = (
        torch.stack([torch.tensor(pair[0]) for pair in valset]),
        torch.tensor([pair[1] for pair in valset])
    )
    testset = val_and_test_set[5000:]
    testset = (
        torch.stack([torch.tensor(pair[0]) for pair in testset]),
        torch.tensor([pair[1] for pair in testset])
    )

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

class NeuralNet(nn.Module):

    def __init__(self, layer_sizes):

        super().__init__()

        self.weight1 = nn.Parameter(torch.randn(layer_sizes[0],layer_sizes[1]));
        self.bias1= nn.Parameter(torch.randn(layer_sizes[1]));
        self.weight2 = nn.Parameter(torch.randn(layer_sizes[1],layer_sizes[2]));
        self.bias2 = nn.Parameter(torch.randn(layer_sizes[2]));

        self.sigmoid = nn.Sigmoid()

    def forward(self, images):

        a = self.sigmoid(torch.matmul(images, self.weight1) + self.bias1);
        b = self.sigmoid(torch.matmul(a, self.weight2) + self.bias2);
        return b;

def reshape(images):
    '''
    Reshapes a set of images of the shape (batch_size, width, height, channels)
    into the proper shape (batch_size, width * height * channels) that the model can accept.
    '''
    return images.reshape(images.shape[0], -1).float()

EPOCHS = 10 #
LEARNING_RATE = 0.01
HIDDEN_LAYER_SIZES = [32 * 32 * 3, 40, 10]

net = NeuralNet(HIDDEN_LAYER_SIZES)
optimizer = torch.optim.Adam(net.parameters(), lr=LEARNING_RATE)
loss_fn = nn.CrossEntropyLoss()

print(net)

for epoch in range(EPOCHS):

    average_loss = 0

    for images, labels in trainloader:

        images = reshape(images)
        output = net(images)
        loss = loss_fn(output, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        average_loss += loss.item()

    average_loss /= len(trainloader)

    val_output = net(reshape(valset[0]))
    val_loss = loss_fn(val_output, valset[1]).item()

    print("(epoch, train_loss, val_loss) = ({0}, {1}, {2})".format(epoch, average_loss, val_loss))

### Accuracy of Model ###
test_output = net(reshape(testset[0]))
test_maxes = torch.argmax(test_output, dim=1)
print("Test accuracy:", torch.sum(test_maxes == testset[1]).item() / float(test_maxes.shape[0]))
