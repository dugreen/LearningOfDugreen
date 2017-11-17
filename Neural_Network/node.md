# 在Python中从头开始实现一个神经网络——介绍
# Implementing a Neural Network from Scratch in Python – An Introduction

在这篇文章中，我们将从头开始实现一个简单的三层神经网络。我们不会推导出所有需要的数学，但我会试着直观地解释一下我们在做什么。我还将向您介绍有关详细信息的参考资料。
在这里，我假设您熟悉基本的微积分和机器学习概念，例如，您知道什么是分类和规则化。理想情况下，您还可以了解一些优化技术，如梯度下降工作。但即使你不熟悉上面的任何一篇文章，你仍然会发现它很有趣;
但是，为什么要从头开始实现一个神经网络呢?即使您计划将来使用像PyBrain这样的神经网络库，至少从头开始实现一个网络是一个非常有价值的练习。它帮助你了解神经网络是如何工作的，这对于设计有效的模型是非常重要的。
需要注意的一点是，这里的代码示例并不是特别有效。它们本应易于理解。在即将发布的一篇文章中，我将探讨如何使用Theano编写一个高效的神经网络实现。(更新:现在可用)
In this post we will implement a simple 3-layer neural network from scratch. We won’t derive all the math that’s required, but I will try to give an intuitive explanation of what we are doing. I will also point to resources for you read up on the details.

Here I’m assuming that you are familiar with basic Calculus and Machine Learning concepts, e.g. you know what classification and regularization is. Ideally you also know a bit about how optimization techniques like gradient descent work. But even if you’re not familiar with any of the above this post could still turn out to be interesting ;)

But why implement a Neural Network from scratch at all? Even if you plan on using Neural Network libraries like PyBrain in the future, implementing a network from scratch at least once is an extremely valuable exercise. It helps you gain an understanding of how neural networks work, and that is essential for designing effective models.


One thing to note is that the code examples here aren’t terribly efficient. They are meant to be easy to understand. In an upcoming post I will explore how to write an efficient Neural Network implementation using Theano. (Update: now available)


生成数据集
Generating a dataset

让我们从生成一个可以使用的数据集开始。幸运的是，scikit- learn有一些有用的数据集生成器，因此我们不需要自己编写代码。我们将使用make_月亮函数。
Let’s start by generating a dataset we can play with. Fortunately, scikit-learn has some useful dataset generators, so we don’t need to write the code ourselves. We will go with the make_moons function.

# Generate a dataset and plot it
np.random.seed(0)2
X, y = sklearn.datasets.make_moons(200, noise=0.20)
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)

我们生成的数据集有两个类，绘制成红色和蓝色的点。你可以把蓝点看成是男性患者，红点是女性患者，x和y轴是医学测量。
我们的目标是训练一个机器学习分类器，该分类器可以根据x和y坐标预测正确的类(女性的男性)。注意，数据不是线性可分的，我们不能画一条直线将这两个类分开。这意味着线性分类器，如逻辑回归，将无法与数据相匹配，除非您手工设计非线性特性(如多项式)，这对给定的数据集很有效。
事实上，这是神经网络的主要优势之一。您不必担心功能工程。神经网络的隐藏层将为您学习特性。
The dataset we generated has two classes, plotted as red and blue points. You can think of the blue dots as male patients and the red dots as female patients, with the x- and y- axis being medical measurements.

Our goal is to train a Machine Learning classifier that predicts the correct class (male of female) given the x- and y- coordinates. Note that the data is not linearly separable, we can’t draw a straight line that separates the two classes. This means that linear classifiers, such as Logistic Regression, won’t be able to fit the data unless you hand-engineer non-linear features (such as polynomials) that work well for the given dataset.

In fact, that’s one of the major advantages of Neural Networks. You don’t need to worry about feature engineering. The hidden layer of a neural network will learn features for you.

逻辑回归
Logistic Regression


为了证明这一点，我们来训练一个逻辑回归分类器。它的输入将是x和y值，输出预测的类(0或1)。为了使我们的生活更容易，我们使用scikit- learn的Logistic回归类。
To demonstrate the point let’s train a Logistic Regression classifier. It’s input will be the x- and y-values and the output the predicted class (0 or 1). To make our life easy we use the Logistic Regression class from scikit-learn.

# Train the logistic rgeression classifier
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)
 
# Plot the decision boundary
plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")

该图形显示了Logistic回归分类器学习的决策边界。它将数据与使用直线的数据区分开来，但它无法捕捉到我们数据的“月球形状”。
The graph shows the decision boundary learned by our Logistic Regression classifier. It separates the data as good as it can using a straight line, but it’s unable to capture the “moon shape” of our data.


训练一个神经网络
Training a Neural Network

现在，让我们构建一个具有一个输入层、一个隐藏层和一个输出层的3层神经网络。输入层的节点数由我们的数据的维数决定，2。类似地，输出层中的节点数量由我们拥有的类的数量决定，也就是2。(因为我们只有2个类，实际上只有一个输出节点预测0或1，但是有2个类可以更容易地将网络扩展到以后的更多类)。网络的输入将是x - y坐标，它的输出将是两个概率，一个为0(“女性”)，另一个为类1(“男性”)。它看起来是这样的:
Let’s now build a 3-layer neural network with one input layer, one hidden layer, and one output layer. The number of nodes in the input layer is determined by the dimensionality of our data, 2. Similarly, the number of nodes in the output layer is determined by the number of classes we have, also 2. (Because we only have 2 classes we could actually get away with only one output node predicting 0 or 1, but having 2 makes it easier to extend the network to more classes later on). The input to the network will be x- and y- coordinates and its output will be two probabilities, one for class 0 (“female”) and one for class 1 (“male”). It looks something like this:


我们可以选择隐藏层的维数(节点数)。我们将更多的节点放入隐藏层中，我们将会有更复杂的功能。但更高的维度是有代价的。首先，需要更多的计算来预测和学习网络参数。更大的参数也意味着我们变得更容易过度拟合我们的数据。
如何选择隐藏层的大小?虽然有一些一般的指导方针和建议，但它总是取决于你的具体问题，而不仅仅是一门科学。稍后我们将使用隐藏的节点数量，看看它如何影响我们的输出。
我们还需要为隐藏层选择一个激活函数。激活函数将层的输入转换为输出。一个非线性的激活函数使我们能够适应非线性假设。激活函数的常见选择是tanh,sigmoid函数，或ReLUs。我们将使用tanh，它在很多场景中都表现得很好。这些函数的一个很好的性质是，它们的派生可以使用原始函数值来计算。例如,1 - \ \双曲正切x的导数是双曲正切^ 2 x。这很有用,因为它允许我们计算\双曲正切x一旦和重用其价值以后导数。
因为我们希望我们的网络输出概率，输出层的激活函数将是softmax，它只是将原始分数转换成概率的一种方式。如果您熟悉logistic函数，您可以将softmax看作是它对多个类的泛化。

We can choose the dimensionality (the number of nodes) of the hidden layer. The more nodes we put into the hidden layer the more complex functions we will be able fit. But higher dimensionality comes at a cost. First, more computation is required to make predictions and learn the network parameters. A bigger number of parameters also means we become more prone to overfitting our data.

How to choose the size of the hidden layer? While there are some general guidelines and recommendations, it always depends on your specific problem and is more of an art than a science. We will play with the number of nodes in the hidden later later on and see how it affects our output.

We also need to pick an activation function for our hidden layer. The activation function transforms the inputs of the layer into its outputs. A nonlinear activation function is what allows us to fit nonlinear hypotheses. Common chocies for activation functions are tanh, the sigmoid function, or ReLUs. We will use tanh, which performs quite well in many scenarios. A nice property of these functions is that their derivate can be computed using the original function value. For example, the derivative of \tanh x is 1-\tanh^2 x. This is useful because it allows us to compute \tanh x  once and re-use its value later on to get the derivative.

Because we want our network to output probabilities the activation function for the output layer will be the softmax, which is simply a way to convert raw scores to probabilities. If you’re familiar with the logistic function you can think of softmax as its generalization to multiple classes.

我们的网络是如何预测的
我们的网络利用正向传播进行预测，它只是一堆矩阵乘法和我们在上面定义的激活函数的应用。如果x是我们网络的二维输入，那么我们计算我们的预测\帽{y}(也就是二维)如下:
How our network makes predictions

Our network makes predictions using forward propagation, which is just a bunch of matrix multiplications and the application of the activation function(s) we defined above. If x is the 2-dimensional input to our network then we calculate our prediction \hat{y} (also two-dimensional) as follows:


z_i是图层i和a_i的输入，是在应用激活函数后的图层i的输出。W_1、b_1、W_2、b_2是我们网络的参数，我们需要从训练数据中学习。你可以把它们看作是矩阵在网络层之间转换数据的矩阵。看看上面的矩阵乘法我们就能求出这些矩阵的维数。如果我们使用500节点隐藏层然后W_1 \ \ mathbb { R } ^ { 2 \ times500 },b_1 \中\ mathbb { R } ^ { 500 },在W_2 \ \ mathbb { R } ^ { 500 \ times2 },b_2 \中\ mathbb { R } ^ { 2 }。现在你明白了为什么我们有更多的参数如果我们增加隐藏层的尺寸。

z_i is the input of layer i and a_i is the output of layer i after applying the activation function. W_1, b_1, W_2, b_2 are parameters of our network, which we need to learn from our training data. You can think of them as matrices transforming data between layers of the network. Looking at the matrix multiplications above we can figure out the dimensionality of these matrices. If we use 500 nodes for our hidden layer then W_1 \in \mathbb{R}^{2\times500}, b_1 \in \mathbb{R}^{500}, W_2 \in \mathbb{R}^{500\times2}, b_2 \in \mathbb{R}^{2}. Now you see why we have more parameters if we increase the size of the hidden layer.

学习参数
为我们的网络学习参数意味着寻找参数(W_1,b_1,W_2,b_2)，使训练数据的错误最小化。但是我们如何定义错误呢?我们称函数为测量误差的函数。软最大值输出的一个常见选择是分类交叉熵损失(也称为负对数似然)。如果我们有N个训练样本和C类，那么我们对y标签的预测损失就会得到:
Learning the Parameters

Learning the parameters for our network means finding parameters (W_1, b_1, W_2, b_2) that minimize the error on our training data. But how do we define the error? We call the function that measures our error the loss function. A common choice with the softmax output is the categorical cross-entropy loss (also known as negative log likelihood). If we have N training examples and C classes then the loss for our prediction \hat{y} with respect to the true labels y is given by:


这个公式看起来很复杂，但它真正做的是对我们的训练示例进行求和，如果我们预测了不正确的类，就会增加损失。越远的两个概率分布y(正确的标签)和(我们的预测)，我们的损失越大。通过寻找最小化损失的参数，我们就能最大限度地提高训练数据的可能性。
我们可以使用梯度下降法来找到最小值，我将实现最基本的梯度下降法，也叫批量梯度下降，固定学习速率。在实践中，SGD(随机梯度下降)或minibatch梯度下降等变体通常表现得更好。所以如果你认真的话，你会想要使用其中的一个，理想情况下，你也会随着时间的推移而衰减学习速率。
作为一种输入，梯度下降需要有关参数的损失函数的梯度(导数的向量):\ frac {\部分{} {\部分{}} {\ {} {\ {} {} {{} {} {} {} {{} {} {} {{} {} {} {} {} {} {} {} {{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {为了计算这些梯度，我们使用了著名的反向传播算法，这是一种有效地计算从输出开始的梯度的方法。我不会详细介绍反向传播是如何工作的，但在web上有许多优秀的解释(这里或这里)。
应用反向传播公式，我们找到以下方法(相信我):
The formula looks complicated, but all it really does is sum over our training examples and add to the loss if we predicted the incorrect class. The further away the two probability distributions y (the correct labels) and \hat{y} (our predictions) are, the greater our loss will be. By finding parameters that minimize the loss we maximize the likelihood of our training data.


We can use gradient descent to find the minimum and I will implement the most vanilla version of gradient descent, also called batch gradient descent with a fixed learning rate. Variations such as SGD (stochastic gradient descent) or minibatch gradient descent typically perform better in practice. So if you are serious you’ll want to use one of these, and ideally you would also decay the learning rate over time.

As an input, gradient descent needs the gradients (vector of derivatives) of the loss function with respect to our parameters: \frac{\partial{L}}{\partial{W_1}}, \frac{\partial{L}}{\partial{b_1}}, \frac{\partial{L}}{\partial{W_2}}, \frac{\partial{L}}{\partial{b_2}}. To calculate these gradients we use the famous backpropagation algorithm, which is a way to efficiently calculate the gradients starting from the output. I won’t go into detail how backpropagation works, but there are many excellent explanations (here or here) floating around the web.

Applying the backpropagation formula we find the following (trust me on this):

实现
现在我们已经做好了实现的准备。我们首先定义一些有用的变量和梯度下降的参数:
Implementation

Now we are ready for our implementation. We start by defining some useful variables and parameters for gradient descent:


我们还实现了一个帮助函数来计算网络的输出。它向前定义了传播，并以最高的概率返回类。
We also implement a helper function to calculate the output of the network. It does forward propagation as defined above and returns the class with the highest probability.